from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('author', 'created_at', 'updated_at')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'author_id', 'title', 'content', 'image',
            'created_at', 'updated_at', 'comments', 'comments_count'
        )
        read_only_fields = ('author', 'created_at', 'updated_at', 'comments')

    def get_comments_count(self, obj):
        return obj.comments.count()
