"""
URL configuration for minincode24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from main.views import index
from django.conf import settings
import re
from django.views.static import serve

urlpatterns = [
    path('api/', include("main.urls")),
    path('', index),
    re_path(r"^%s(?P<path>.*)$" % re.escape(settings.STATIC_URL.lstrip("/")), serve,
            kwargs={'document_root': settings.STATIC_ROOT}),
    re_path(r"^%s(?P<path>.*)$" % re.escape(settings.MEDIA_URL.lstrip("/")), serve,
            kwargs={'document_root': settings.MEDIA_ROOT}),
]
