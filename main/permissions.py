from rest_framework.permissions import BasePermission
from .models import User, News
import json


class Admin(BasePermission):
    def has_permission(self, request, view):
        try:
            return not request.session['is_auth'] is None
        except KeyError:
            return False


class NewsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            if not request.session['is_auth'] is None:
                user_id = int(request.session['is_auth'])
                if request.method == 'PATCH' or request.method == 'PUT':
                    data = str(request.body, 'utf-8')
                    post_data = json.loads(data)
                    news_id = str(post_data['news_id']).strip()
                    news = News.objects.get(pk=int(news_id))
                    return news.organization_id == user_id
                user = User.objects.get(pk=int(user_id))
                return user.type == 'organization'
        except KeyError:
            return False


class EventsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            if not request.session['is_auth'] is None:
                user_id = int(request.session['is_auth'])
                if request.method == 'PATCH' or request.method == 'PUT':
                    data = str(request.body, 'utf-8')
                    post_data = json.loads(data)
                    event_id = str(post_data['event_id']).strip()
                    event = News.objects.get(pk=int(event_id))
                    return event.organization_id == user_id
                user = User.objects.get(pk=int(user_id))
                return user.type == 'organization'
        except KeyError:
            return False


class Any(BasePermission):
    def has_permission(self, request, view):
        return True
