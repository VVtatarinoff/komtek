from rest_framework import serializers

from references.models import RefVersions, RefTitles


# class ReferenceSerializer(serializers.ModelSerializer):
#     """Сериализатор для списка словарей"""
#
#     class Meta:
#         model = RefTitles
#         fields = ['id', 'name', 'short_name', 'description']


class ReferenceSerializer(serializers.ModelSerializer):
    version_name = serializers.CharField()
    version_id = serializers.IntegerField()
    valid_date = serializers.DateField()

    class Meta:
        model = RefTitles
        fields = ['id', 'name', 'short_name', 'description', 'version_name', 'version_id', 'valid_date']
