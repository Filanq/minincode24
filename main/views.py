from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .permissions import NewsAdmin, Any, EventsAdmin, Admin
from django.contrib.auth.hashers import make_password, check_password
from .models import User, News, Event
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import NewsSerializer, EventsSerializer, UsersSerializer


# News List
class NewsList(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [Any()]
        return [NewsAdmin()]

# Events List
class EventsList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [Any()]
        return [EventsAdmin()]

# Users List
class UsersList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [Any()]
        return [Admin()]

# Index View
def index(request):
    return render(request, "main/dist/index.html")


# Login View
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = str(request.body, 'utf-8')
        post_data = json.loads(data)
        email = str(post_data['email']).strip()
        password = str(post_data['password']).strip()

        # Validate
        if not email:
            return HttpResponse(json.dumps({"result": False, 'error': 'Введите Email'}),
                                content_type='application/json')
        if not password:
            return HttpResponse(json.dumps({"result": False, 'error': 'Введите пароль'}),
                                content_type='application/json')

        # Сheck for User
        user = User.objects.filter(email=email)
        if user.exists():
            if check_password(password, user[0].password):
                request.session['is_auth'] = user[0].pk
                return HttpResponse(json.dumps({"result": True, 'error': ''}),
                                    content_type='application/json')
        return HttpResponse(json.dumps({"result": False, 'error': 'Пользователь с такими данными не найден'}),
                            content_type='application/json')

# Register View
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = str(request.body, 'utf-8')
        post_data = json.loads(data)
        firstname = ''
        surname = ''
        lastname = ''
        email = str(post_data['email']).strip()
        password = str(post_data['password']).strip()
        type = str(post_data['type']).strip()
        name = ''
        website = ''
        address = ''

        if type == 'user':
            firstname = str(post_data['firstname']).strip()
            surname = str(post_data['surname']).strip()
            lastname = str(post_data['lastname']).strip()

            if not firstname:
                return HttpResponse(json.dumps({"result": False, 'error': 'Введите имя'}),
                                    content_type='application/json')
            if not surname:
                return HttpResponse(json.dumps({"result": False, 'error': 'Введите фамилию'}),
                                    content_type='application/json')
        elif type == 'organization':
            name = str(post_data['name']).strip()
            website = str(post_data['website']).strip()
            address = str(post_data['address']).strip()

            if not name:
                return HttpResponse(json.dumps({"result": False, 'error': 'Введите название организации'}),
                                    content_type='application/json')
            if not address:
                return HttpResponse(json.dumps({"result": False, 'error': 'Введите адрес организации'}),
                                    content_type='application/json')

        # Validate
        if not email:
            return HttpResponse(json.dumps({"result": False, 'error': 'Введите Email'}),
                                content_type='application/json')
        if len(email) < 6 or not '@' in email or not '.' in email:
            return HttpResponse(json.dumps({"result": False, 'error': 'Email невалиден'}),
                                content_type='application/json')
        if not password:
            return HttpResponse(json.dumps({"result": False, 'error': 'Введите пароль'}),
                                content_type='application/json')
        if len(password) < 8:
            return HttpResponse(json.dumps({"result": False, 'error': 'Мин. длинна пароля - 8 символов'}),
                                content_type='application/json')

        # Сheck for User
        user = User.objects.filter(email=email)
        if user.exists():
            return HttpResponse(json.dumps({"result": False, 'error': 'Пользователь с такой почтой уже существует'}),
                                content_type='application/json')
        else:
            if type == 'user':
                User(firstname=firstname, surname=surname, lastname=lastname, email=email,
                     password=make_password(password), type=type, verified=True).save()
                request.session['is_auth'] = True
                return HttpResponse(json.dumps({"result": True, 'error': ''}),
                                content_type='application/json')
            elif type == 'organization':
                User(name=name, website=website, address=address, email=email,
                     password=make_password(password), type=type, verified=False).save()
                return HttpResponse(json.dumps({"result": True, 'error': ''}),
                                content_type='application/json')


    return HttpResponse(json.dumps({"result": False, 'error': 'Ошибка сервера. Попробуйте позже'}),
                        content_type='application/json')

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        request.session['is_auth'] = None


# Auth Checker View
def auth(request):
    try:
        if request.session['is_auth']:
            return HttpResponse(json.dumps({'is_auth': True}), content_type='application/json')
    except KeyError:
        pass

    return HttpResponse(json.dumps({'is_auth': False}), content_type='application/json')
