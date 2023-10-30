from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',  # Django automatically creates an ID for each model
            'code',
            'host',
            'guest_can_pause',
            'votes_to_skip',
            'created_at',
        )