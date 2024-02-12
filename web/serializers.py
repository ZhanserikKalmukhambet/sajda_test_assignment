from rest_framework import serializers
from web.models import Hadith, Surah, Dhikr, Ayah, UserDhikrRead


class HadithSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hadith
        fields = '__all__'


class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surah
        fields = '__all__'


class DhikrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dhikr
        fields = '__all__'


class DhikrReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDhikrRead
        fields = '__all__'


class AyahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayah
        fields = '__all__'


