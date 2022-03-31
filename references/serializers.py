from rest_framework import serializers

from references.models import RefVersions


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefVersions
        fields = ('reference', 'version', 'init_date')