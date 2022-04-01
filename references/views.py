from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.views import APIView

from references.models import RefVersions, RefTitles
from references.serializers import ReferenceSerializer


class ReferencesAPIView(generics.ListAPIView):
    """ Прдоставляет ответ на GET запрос со списком словарей
    в параметрах запроса может указываться дата в формате date = YYY-MM-DD,
    если дата не указана, то принимается текущая дата.
    Список словарей выдается актуальным на эту дату

    Список выдается с pagination = 10"""

    serializer_class = ReferenceSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date', datetime.date(datetime.now()))
        valid_versions = RefVersions.objects.filter(
            init_date__lte=date).order_by(
            'reference_id', '-init_date').distinct('reference_id').values_list('reference', flat=True)
        return RefTitles.objects.filter(id__in=valid_versions)
