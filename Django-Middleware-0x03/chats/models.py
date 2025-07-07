from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# create user model
class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    user_id  = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True, 
        primary_key=True
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)


# create conversation model
class Conversation(models.Model):
    """
    Model representing a conversation between users.
    """
    conversation_id = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True, 
        primary_key=True
    )
    participants = models.ManyToManyField(User, related_name='conversations')

    def __str__(self):
        return f"Conversation {self.id} with {self.participants.count()} participants"
    

# create message model
class Message(models.Model):
    """
    Model representing a message in a conversation.
    """
    message_id = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True, 
        primary_key=True
    )
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f"Message {self.id} from {self.sender.username} in Conversation {self.conversation.id}"