from rest_framework import generics
from rest_framework.generics import ListAPIView
from .serializers import  UserSerializer
from .models import User
from posts.models import Post
from posts.serializers import PostSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class UserPostsListView(ListAPIView): #로그인한 유저가 작성한 게시물 모아보기
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
class LikedPostsListView(generics.ListAPIView): #로그인한 유저가 좋아요 누른 게시물 모아보기
    serializer_class = PostSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(like__user=user)