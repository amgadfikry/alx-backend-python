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
    """
    Serializer for Message model.
    Includes nested sender information.
    """
    sender = UserSerializer(read_only=True)  # show sender as nested object
    sender_id = serializers.UUIDField(write_only=True)  # allow sender_id input during creation
    conversation_id = serializers.UUIDField(write_only=True)  # allow linking to conversation

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


#  Conversation Serializer
class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for Conversation model.
    Includes nested users and all related messages.
    """
    participants = UserSerializer(many=True, read_only=True)
    participant_ids = serializers.ListField(
        child=serializers.UUIDField(), write_only=True,
        required=False,
        help_text="List of user UUIDs to add as participants"
    )
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'participant_ids',
            'messages'
        ]
        read_only_fields = ['conversation_id']

    def create(self, validated_data):
        """
        Custom creation logic to handle ManyToManyField (participants).
        """
        participant_ids = validated_data.pop('participant_ids', [])
        conversation = Conversation.objects.create(**validated_data)
        if participant_ids:
            users = User.objects.filter(user_id__in=participant_ids)
            conversation.participants.set(users)
        return conversation
