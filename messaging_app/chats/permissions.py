from rest_framework.permissions import BasePermission

class IsOwnerOrParticipant(BasePermission):
    """
    Allows access only to the owner of the conversation or a participant in the message.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        # For Conversation model (example)
        if hasattr(obj, 'participants'):
            return user in obj.participants.all()
        # For Message model (example)
        elif hasattr(obj, 'sender'):
            return obj.sender == user or user in obj.conversation.participants.all()
        return False