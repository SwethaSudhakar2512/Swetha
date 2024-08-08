from rest_framework import generics, permissions
from .models import Interest, Message
from .serializers import UserSerializer, InterestSerializer, MessageSerializer
from django.contrib.auth.models import User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class InterestListCreate(generics.ListCreateAPIView):
    serializer_class = InterestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Interest.objects.filter(receiver=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class InterestUpdate(generics.RetrieveUpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
