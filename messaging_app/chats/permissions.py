# chats/permissions.py

from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsOwnerOrParticipant(BasePermission):
    """
    Custom permission to only allow owners/participants to access conversations or messages.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'participants'):
            return user in obj.participants.all()

        elif hasattr(obj, 'sender') and hasattr(obj, 'conversation'):
            return obj.sender == user or user in obj.conversation.participants.all()

        return False
