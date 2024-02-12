from django.urls import path
from rest_framework.routers import DefaultRouter
from web.views import HadithViewSet, DhikrViewSet, SurahViewSet

urlpatterns = [
]

r = DefaultRouter()

r.register(r'hadiths', HadithViewSet, basename='hadith')
r.register(r'surahs', SurahViewSet, basename='surah')
r.register(r'dhikrs', DhikrViewSet, basename='dhikr')

urlpatterns += r.urls
