from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=250, null=False)


# class Profession(models.Model):
#     title = models.CharField(max_length=250, null=True)
#     text = models.TextField(max_length=1000, null=True)
#     img1 = models.ImageField(blank=True, null=True, upload_to='professions')
#     img2 = models.ImageField(blank=True, null=True, upload_to='professions')
