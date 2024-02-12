from django.contrib import admin
from .models import Surah, Ayah, Dhikr, Hadith, UserDhikrRead, SharedSurah, SharedHadith

# Register your models here.


admin.site.register(Surah)
admin.site.register(Ayah)
admin.site.register(Dhikr)
admin.site.register(Hadith)
admin.site.register(UserDhikrRead)
admin.site.register(SharedSurah)
admin.site.register(SharedHadith)
