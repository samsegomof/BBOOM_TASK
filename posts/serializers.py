from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post

#USER_MODEL = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username')

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body')


class PostCreateSerializer(PostSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('author', 'title', 'body')