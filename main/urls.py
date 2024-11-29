from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login, auth, register, logout, UsersList, NewsList, EventsList, accept_org, EventRequestsList, OrganizationList

router = DefaultRouter()
router.register('users', UsersList)
router.register('news', NewsList)
router.register('events', EventsList)
router.register('events-req', EventRequestsList)
router.register('organization', OrganizationList)

urlpatterns = [
    path('', include(router.urls)),
    path('login', login),
    path('register', register),
    path('logout', logout),
    path('auth', auth),
    path('accept-org', accept_org)
]
