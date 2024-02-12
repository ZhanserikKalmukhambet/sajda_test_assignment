from django.urls import path
from rest_framework.routers import DefaultRouter
from web.views import HadithViewSet, DhikrViewSet, SurahViewSet, UserDhikrReadViewSet

urlpatterns = [
    path('users/<int:pk>/dhikr/add/', UserDhikrReadViewSet.as_view({'post': 'create'})),
    path('users/<int:pk_1>/dhikr/<int:pk_2>/update/', UserDhikrReadViewSet.as_view({'patch': 'update'}))
]

r = DefaultRouter()
r.register(r'hadiths', HadithViewSet, basename='hadith')
r.register(r'surahs', SurahViewSet, basename='surah')
r.register(r'dhikrs', DhikrViewSet, basename='dhikr')

urlpatterns += r.urls
