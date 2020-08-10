from rest_framework import serializers
from .models import (
    Comment,
    Video,
    VideoViewed,
)


class CommentSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "video", "user", "comment", "created_at", "updated_at",)



class VideoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, queryset=Comment.objects.all())
    class Meta:
        model = Video
        fields = ("id", "title", "views", "author", "youtube_id", "active",
                  "thumbnail_url", "slug", "likes", "dislikes", "comments",
                  "publicado",)


class VideoViewedSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    class Meta:
        model = VideoViewed
        fields = ("id", "video", "viewed_at",)
