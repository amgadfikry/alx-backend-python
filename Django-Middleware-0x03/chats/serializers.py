# chats/serializers.py

from rest_framework import serializers
from .models import User, Conversation, Message


# User Serializer

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    Excludes password from the output.
    """
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number']
        read_only_fields = ['user_id']


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.UUIDField(write_only=True)
    conversation_id = serializers.UUIDField(write_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = [
            'message_id',
            'message_body',
            'sent_at',
            'created_at',
            'sender',
            'sender_id',
            'conversation_id',
        ]
        read_only_fields = ['message_id', 'sent_at', 'created_at']

    def validate_message_body(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Message cannot be empty or whitespace.")
        return value


#  Conversation Serializer
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    participant_ids = serializers.ListField(
        child=serializers.UUIDField(), write_only=True, required=False
    )
    messages = MessageSerializer(many=True, read_only=True)
    total_messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'participant_ids',
            'messages',
            'total_messages'  # new field
        ]
        read_only_fields = ['conversation_id']

    def get_total_messages(self, obj):
        return obj.messages.count()

    def create(self, validated_data):
        participant_ids = validated_data.pop('participant_ids', [])
        conversation = Conversation.objects.create(**validated_data)
        if participant_ids:
            users = User.objects.filter(user_id__in=participant_ids)
            conversation.participants.set(users)
        return conversation

