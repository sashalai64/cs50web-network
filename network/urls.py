
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newPost", views.newPost, name = "newPost"),
    path("like/<int:postId>", views.likePost, name = "likePost"),
    path("unlike/<int:postId>", views.unlikePost, name = "unlikePost"),
    path("edit/<int:postId>", views.edit, name="edit"),
    path("following", views.following, name="following"),
    path("followToggle/<int:userId>", views.follow_toggle, name="follow_toggle"),
    path("profile/<int:userId>", views.profile, name="profile")
]
