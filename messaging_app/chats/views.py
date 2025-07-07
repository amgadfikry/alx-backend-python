from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for sending and listing messages.
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

    def get_queryset(self):
        conversation_id = self.kwargs.get("conversation_id")
        if not conversation_id:
            return Message.objects.none()

        queryset = Message.objects.filter(conversation__id=conversation_id)

        if not queryset.exists():
            return Message.objects.none()

        # Enforce participant-only access
        if self.request.user not in queryset.first().conversation.participants.all():
            return Message.objects.none()

        return queryset

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get('conversation')

        if self.request.user not in conversation.participants.all():
            return Response({'detail': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        serializer.save(sender=self.request.user)
