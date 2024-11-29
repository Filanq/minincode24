from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=250, null=False)
    type = models.CharField(max_length=100, null=False, default='user')
    name = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    website = models.CharField(max_length=250, null=True)
    verified = models.BooleanField(default=False)


class News(models.Model):
    title = models.CharField(max_length=250, null=True)
    text = models.TextField(max_length=1000, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='news')
    date = models.DateField(null=True)
    organization = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)


class Event(models.Model):
    title = models.CharField(max_length=250, null=True)
    text = models.TextField(max_length=1000, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='events')
    datetime = models.DateTimeField(null=True)
    address = models.CharField(max_length=250, null=True)
    count = models.IntegerField(null=False)
    organization = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)


class EventRequest(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, null=True)


class Organization(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=1000, null=True)
    contacts = models.CharField(max_length=250, null=True)
