from rest_framework import serializers

from references.models import RefVersions, RefTitles


class ReferenceSerializer(serializers.ModelSerializer):
    """Сериализатор для списка словарей"""
    class Meta:
        model = RefTitles
        fields = '__all__'



