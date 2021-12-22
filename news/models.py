from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField()
    author = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
