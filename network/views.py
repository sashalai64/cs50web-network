from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *


def index(request):
    all_posts = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    likes = Like.objects.all()

    #posts that you liked
    liked = []
    if request.user.is_authenticated:
        for like in likes:
            if like.user.id == request.user.id:
                liked.append(like.post.id)

    #save number of likes for posts
    for post in posts:
        post.likes = Like.objects.filter(post = post).count()
        post.save()

    return render(request, "network/index.html", {
        "posts": posts,
        "liked": liked,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def newPost(request):
   if request.method == 'POST':
       user = request.user
       content = request.POST['content']
       if content == '':
           return render(request, 'network/index.html', {
               'message': "Post content cannot be empty."
           })
       post = Post(user = user, content = content)
       post.save()
       return HttpResponseRedirect(reverse(index))
   

@login_required
def likePost(request, postId):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id = postId)
        like = Like(user = user, post = post)
        like.save()

        likes = Like.objects.filter(post = post).count()
        
        return JsonResponse({
            "message": "Like added.",
            "likes": likes
        })


@login_required
def unlikePost(request, postId):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id = postId)
        like = Like.objects.filter(user = user, post = post)
        like.delete()
        
        likes = Like.objects.filter(post = post).count()
        
        return JsonResponse({
            "message": "Like removed.",
            "likes": likes
        })
    

@login_required
@csrf_exempt
def edit(request, postId):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = request.user
        post = Post.objects.get(id = postId)

        if user == post.user:
            content = body['content']
            post.content = content
            post.save()
            return JsonResponse({
                "message": "Changes saved.",
                "content": content
            })
        else:
            return JsonResponse({"message": "You cannot edit this post."}, status = 403)