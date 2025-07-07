# 0x03-MessagingApp-Django/chats/middleware.py

import logging
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        # Allow access only between 18:00 (6 PM) and 21:00 (9 PM)
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Access to messaging is allowed only between 6 PM and 9 PM.")

        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = {}  # {ip_address: [timestamp, ...]}

    def __call__(self, request):
        # Only apply rate limiting to POST requests to the message endpoint
        if request.method == 'POST' and request.path.startswith('/api/messages'):
            ip = self.get_ip(request)
            now = datetime.now()

            if ip not in self.message_log:
                self.message_log[ip] = []

            # Remove timestamps older than 1 minute
            self.message_log[ip] = [
                ts for ts in self.message_log[ip]
                if now - ts < timedelta(minutes=1)
            ]

            # If more than 5 requests in the last minute, block
            if len(self.message_log[ip]) >= 5:
                return HttpResponseForbidden("Rate limit exceeded: Only 5 messages per minute allowed.")

            # Log the current request
            self.message_log[ip].append(now)

        return self.get_response(request)

    def get_ip(self, request):
        # Get IP address from X-Forwarded-For if behind proxy
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
