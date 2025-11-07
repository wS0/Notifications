from rest_framework import serializers


class NotifySerializer(serializers.Serializer):
    user_id = serializers.CharField()
    title = serializers.CharField(max_length=200)
    message = serializers.CharField()
