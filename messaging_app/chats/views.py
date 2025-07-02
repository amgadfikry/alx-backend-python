# Create your views here.
from rest_framework import viewsets, permissions, status, filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


# ViewSet for Conversations
class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and creating conversations.
    """
    queryset = Conversation.objects.all().prefetch_related('participants', 'messages')
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # You could auto-include the request.user as a participant if needed
        serializer.save()


# ViewSet for Messages
class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for sending and listing messages.
    """
    queryset = Message.objects.all().select_related('sender', 'conversation')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

    def perform_create(self, serializer):
        # Automatically set sender from the current logged-in user
        serializer.save(sender=self.request.user)
