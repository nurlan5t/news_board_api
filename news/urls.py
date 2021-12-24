from django.urls import path, include
from news import views

urlpatterns = [
    path("news/", views.NewsList.as_view()),
    path("new_post/", views.NewsCreate.as_view()),
    path("post/<int:pk>/", views.PostDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("new_comment/", views.CommentCreate.as_view()),
    path("comment/<int:pk>/", views.CommentDetail.as_view()),
    path("news/<int:pk>/vote/", views.VoteCreate.as_view()),
]
