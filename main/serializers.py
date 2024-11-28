from .models import News, Event, User
from rest_framework.serializers import ModelSerializer


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class EventsSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
