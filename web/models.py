from django.db import models

from users.models import User


# Create your models here.


class Surah(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    likes = models.IntegerField(default=0)


class Ayah(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    text = models.TextField()


class Hadith(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    narratorName = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)


class Dhikr(models.Model):
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)


class UserDhikrRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dhikr = models.ForeignKey(Dhikr, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
