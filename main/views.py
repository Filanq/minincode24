from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .permissions import Admin, Any
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import json


# Professions List
# class ProfessionsList(viewsets.ModelViewSet):
#     queryset = Profession.objects.all()
#     serializer_class = ProfessionSerializer
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             return [Any()]
#         return [Admin()]


# Index View
def index(request):
    return render(request, "main/dist/index.html")


# Login View
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
                request.session['is_auth'] = True
                return HttpResponse(json.dumps({"result": True, 'error': ''}),
                                    content_type='application/json')
            else:
                return HttpResponse(json.dumps({"result": False, 'error': 'Пользователь с такими данными не найден'}),
                                    content_type='application/json')


# Register View
def register(request):
    if request.method == 'POST':
        data = str(request.body, 'utf-8')
        post_data = json.loads(data)
        firstname = str(post_data['firstname']).strip()
        surname = str(post_data['surname']).strip()
        lastname = str(post_data['lastname']).strip()
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
            return HttpResponse(json.dumps({"result": False, 'error': 'Пользователь с такой почтой уже существует'}),
                                content_type='application/json')
        else:
            User(firstname=firstname, surname=surname, lastname=lastname, email=email,
                 password=make_password(password)).save()
            request.session['is_auth'] = True
            return HttpResponse(json.dumps({"result": True, 'error': ''}),
                                content_type='application/json')

    return HttpResponse(json.dumps({"result": False, 'error': 'Ошибка сервера. Попробуйте позже'}),
                        content_type='application/json')


# Auth Checker View
def auth(request):
    try:
        if request.session['is_auth']:
            return HttpResponse(json.dumps({'is_auth': True}), content_type='application/json')
    except KeyError:
        pass

    return HttpResponse(json.dumps({'is_auth': False}), content_type='application/json')
