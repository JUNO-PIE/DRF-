from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

class BlogPagination(PageNumberPagination):
    page_size = 3

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = BlogPagination
    
    filter_backends = [SearchFilter]
    search_fields = ['title', 'blog_text']
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)