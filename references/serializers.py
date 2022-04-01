from rest_framework import serializers

from references.models import RefTitles, Elements


class ReferenceSerializer(serializers.ModelSerializer):
    """Сериализатор для головы справочника и его определенной версии"""

    version_name = serializers.CharField()
    version_id = serializers.IntegerField()
    valid_date = serializers.DateField()

    class Meta:
        model = RefTitles
        fields = ['id', 'name', 'short_name',
                  'description', 'version_name',
                  'version_id', 'valid_date']


class ElementsSerializer(serializers.ModelSerializer):
    """Сериализатор для элементов справочника"""

    class Meta:
        model = Elements
        fields = ['id', 'code', 'value']
