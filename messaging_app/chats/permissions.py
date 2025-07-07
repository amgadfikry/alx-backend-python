from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants in a conversation
    to access messages related to it.
    """

    def has_permission(self, request, view):
        # Only authenticated users are allowed
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Ensure the user is a participant of the conversation
        return request.user in obj.conversation.participants.all()
