from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login, auth, register

router = DefaultRouter()
# router.register('professions', ProfessionsList)

urlpatterns = [
    path('', include(router.urls)),
    path('login', login),
    path('register', register),
    path('auth', auth),
]
