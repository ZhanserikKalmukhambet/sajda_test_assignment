from django.contrib import admin
from .models import Surah, Ayah, Dhikr, Hadith

# Register your models here.


admin.site.register(Surah)
admin.site.register(Ayah)
admin.site.register(Dhikr)
admin.site.register(Hadith)

