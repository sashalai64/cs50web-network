from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "author")
    content = models.TextField(blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return f"Post {self.id} made by {self.user}."


class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "liked_user")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "liked_post")

    def __str__(self):
        return f"{self.user} liked {self.post}."


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "following") #user's following
    following = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "followed") #user's followers

    def __str__(self):
        return f"{self.follower} followed {self.following}."