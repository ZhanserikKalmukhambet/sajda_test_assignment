from rest_framework import viewsets, status
from rest_framework.response import Response

from web.models import Hadith, Surah, Dhikr, Ayah

from web.serializers import HadithSerializer, SurahSerializer, DhikrSerializer, AyahSerializer


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