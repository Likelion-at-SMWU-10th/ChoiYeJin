from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer): # 글 작성
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'body')

class BlogListSerializer(serializers.ModelSerializer): # 글 목록
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'summary')

class CommentSerializer(serializers.ModelSerializer): # 댓글 작성
    class Meta:
        model = Comment
        fields = ('blog', 'id', 'content', 'created_at')