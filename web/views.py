from datetime import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response

from web.models import Hadith, Surah, Dhikr, Ayah, UserDhikrRead

from web.serializers import HadithSerializer, SurahSerializer, DhikrSerializer, AyahSerializer, DhikrReadSerializer


# Create your views here.

class HadithViewSet(viewsets.ModelViewSet):
    serializer_class = HadithSerializer
    queryset = Hadith.objects.all()


class SurahViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Surah.objects.all()
        serializer = SurahSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = Ayah.objects.filter(surah_id=pk)

        print(queryset)

        serializer = AyahSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DhikrViewSet(viewsets.ModelViewSet):
    serializer_class = DhikrSerializer
    queryset = Dhikr.objects.all()


class UserDhikrReadViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        serializer = DhikrReadSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk_1, pk_2):
        try:
            instance = UserDhikrRead.objects.get(user_id=pk_1, dhikr_id=pk_2)
        except UserDhikrRead.DoesNotExist:
            return Response({'error': 'Instance not found'}, status=404)

        instance.timestamp = timezone.now()
        instance.save()

