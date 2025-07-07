import django_filters
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet, DateTimeFromToRangeFilter
import rest_framework.filters as filters
from .models import Message


class MessageFilter(FilterSet):
    created_at = DateTimeFromToRangeFilter()
    sender = filters.NumberFilter(field_name='sender__id')

    class Meta:
        model = Message
        fields = ['sender', 'created_at']