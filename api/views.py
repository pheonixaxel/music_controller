from rest_framework import generics

from api.models import Room
from api.serializers import RoomSerializer


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
