from django.urls import path
from rest_framework.routers import DefaultRouter

from web.views import (AyahViewSet, HadithViewSet, DhikrViewSet, UserDhikrReadViewSet, SurahViewSet, SharedSurahViewSet, SharedHadithViewSet)

urlpatterns = [
    path('ayahs/random/', AyahViewSet.as_view({'get': 'retrieve_random'})),
    path('hadiths/random/', HadithViewSet.as_view({'get': 'retrieve_random'})),

    path('user/dhikr/add/', UserDhikrReadViewSet.as_view({'post': 'create'})),
    path('user/dhikr/<int:pk>/update/', UserDhikrReadViewSet.as_view({'patch': 'update'})),

    path('surah/share/', SharedSurahViewSet.as_view({'post': 'create'})),
    path('hadith/share/', SharedHadithViewSet.as_view({'post': 'create'}))
]

r = DefaultRouter()

r.register(r'dhikrs', DhikrViewSet, basename='dhikr')
r.register(r'surahs', SurahViewSet, basename='surah')

urlpatterns += r.urls
