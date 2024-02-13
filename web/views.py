from django.utils import timezone
from random import choice

from rest_framework import viewsets, status
from web.pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from web.models import (Ayah, Hadith, Dhikr, UserDhikrRead, Surah)
from web.serializers import (AyahSerializer, HadithSerializer, DhikrSerializer, UserDhikrReadSerializer, SurahSerializer, SharedSurahSerializer, SharedHadithSerializer)

# Create your views here.


class AyahViewSet(viewsets.ViewSet):
    def retrieve_random(self, request):
        queryset = choice(Ayah.objects.all())
        serializer = AyahSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HadithViewSet(viewsets.ViewSet):
    def retrieve_random(self, request):
        queryset = choice(Hadith.objects.all())
        serializer = HadithSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DhikrViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dhikr.objects.all()
    serializer_class = DhikrSerializer
    pagination_class = StandardResultsSetPagination


class UserDhikrReadViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        id = request.data.get('dhikr')

        queryset = UserDhikrRead.objects.filter(dhikr=id)
        if queryset.exists():
            return Response({'dhikr': 'already added'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = request.data
            serializer = UserDhikrReadSerializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = UserDhikrRead.objects.get(user_id=request.user.id, dhikr_id=pk)

        serializer = UserDhikrReadSerializer(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(last_read=timezone.now())

        return Response(serializer.data, status=status.HTTP_200_OK)


class SurahViewSet(viewsets.ViewSet):
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        queryset = Surah.objects.all()
        serializer = SurahSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = Ayah.objects.filter(surah_id=pk)

        print(queryset)

        serializer = AyahSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SharedSurahViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def create(self, request):
        data = request.data
        serializer = SharedSurahSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SharedHadithViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def create(self, request):
        data = request.data
        serializer = SharedHadithSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

