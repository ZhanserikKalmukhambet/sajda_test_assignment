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


class UserDhikrReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDhikrRead
        fields = ['dhikr']
        read_only_fields = ['user']

    def create(self, validated_data):
        # Automatically set the authenticated user as the creator of the instance
        user = self.context['request'].user
        return UserDhikrRead.objects.create(user=user, **validated_data)


class AyahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayah
        fields = '__all__'


