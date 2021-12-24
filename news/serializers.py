from rest_framework import serializers
from news.models import Post, Comment, Vote
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "posts"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = serializers.IntegerField(source="comment.count", read_only=True)
    votes = serializers.IntegerField(source="votes.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "votes", "comments", "link", "author", "created"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["content", "author", "created"]


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "comment", "link", "author", "created"]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "link"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]
