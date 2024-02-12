from django.db import models

from users.models import User


# Create your models here.


class Surah(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Ayah(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    numeration = models.IntegerField(default=1, blank=False)
    text = models.TextField()

    def __str__(self):
        return f'{self.surah} - {self.numeration}'


class Hadith(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    narratorName = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Dhikr(models.Model):
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserDhikrRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dhikr = models.ForeignKey(Dhikr, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.dhikr}'


class SharedSurah(models.Model):
    shared_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='surah_shared_by')
    shared_with = models.OneToOneField(User, on_delete=models.CASCADE, related_name='surah_shared_with')
    surah = models.OneToOneField(Surah, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.shared_by} -> {self.shared_with} = {self.surah}'


class SharedHadith(models.Model):
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hadith_shared_by')
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hadith_shared_with')
    hadith = models.ForeignKey(Hadith, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.shared_by} -> {self.shared_with} = {self.hadith}'

