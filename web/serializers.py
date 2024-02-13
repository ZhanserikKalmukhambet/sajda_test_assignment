from rest_framework import serializers
from web.models import Hadith, Surah, Dhikr, Ayah, UserDhikrRead, SharedSurah, SharedHadith


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
        user = self.context['request'].user
        return UserDhikrRead.objects.create(user=user, **validated_data)


class AyahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayah
        fields = '__all__'


class SharedSurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedSurah
        fields = ['id', 'shared_with', 'surah']
        read_only_fields = ['shared_by']

    def create(self, validated_data):
        user = self.context['request'].user
        return SharedSurah.objects.create(shared_by=user, **validated_data)


class SharedHadithSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedHadith
        fields = ['id', 'shared_with', 'hadith']
        read_only_fields = ['shared_by']

    def create(self, validated_data):
        user = self.context['request'].user
        return SharedHadith.objects.create(shared_by=user, **validated_data)


