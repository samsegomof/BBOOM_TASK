from django.urls import path

from .views import PostListView, PostDeleteView, PostCreateView


urlpatterns = [
    path('list/', PostListView.as_view()),
    path('<int:pk>/', PostDeleteView.as_view()),
    path('create/', PostCreateView.as_view()),
]
