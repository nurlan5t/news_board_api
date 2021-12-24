from django.db import models


class Comment(models.Model):
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.user", related_name="posts", on_delete=models.CASCADE
    )
    comment = models.ManyToManyField(Comment, related_name="comments", blank=True)

    class Meta:
        ordering = ["created"]


class Vote(models.Model):
    voter = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
