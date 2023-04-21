from rest_framework import serializers
from .models import CustomUser, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'photo', 'books_borrowed', 'borrowed_history', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'book', 'text', 'stars', 'created_at')
