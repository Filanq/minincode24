from .models import News, Event, User, EventRequest, Organization
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


class EventRequestsSerializer(ModelSerializer):
    class Meta:
        model = EventRequest
        fields = '__all__'


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
