from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required = False)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required = False)
    view_count = serializers.IntegerField()
    writer = serializers.IntegerField()
    bad_post = serializers.BooleanField() #모델에 없는 field 추가해봄

    def create(self, validated_data):
        writer_id = validated_data['writer']
        post = Post.objects.create(
            content = validated_data['content'],
            view_count = validated_data['view_count'],
            writer = User.objects.get(id = writer_id),
        )
        return post
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'