from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Interest, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class InterestSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Interest
        fields = ['id', 'sender', 'receiver', 'accepted']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']
