from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['blog', 'user']

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    comment = CommentSerializer(many=True)
    
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at', 'comment']