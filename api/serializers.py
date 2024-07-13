from rest_framework import serializers
from .models import Comment
from datetime import datetime, timezone

class CommentSerializer(serializers.ModelSerializer):
    time_ago = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'date_posted', 'time_ago']

    def get_time_ago(self, obj):
        now = datetime.now(timezone.utc)
        diff = now - obj.date_posted
        seconds = diff.total_seconds()

        if seconds < 60:
            return f"{int(seconds)} seconds ago"
        elif seconds < 3600:
            return f"{int(seconds / 60)} minutes ago"
        elif seconds < 86400:
            return f"{int(seconds / 3600)} hours ago"
        else:
            return f"{int(seconds / 86400)} days ago"
