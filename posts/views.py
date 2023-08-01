from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, PostCreateSerializer


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PostDeleteView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    def delete(self, request, *args, **kwargs):

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
