from datetime import datetime

from django.db.models import Subquery, OuterRef
from rest_framework import generics
from rest_framework.views import APIView

from references.models import RefVersions, RefTitles, Elements
from references.serializers import ReferenceSerializer, ElementsSerializer


class ReferencesAPIView(generics.ListAPIView):
    """ Предоставляет ответ на GET запрос со списком словарей
    в параметрах запроса может указываться дата в формате date = YYY-MM-DD,
    если дата не указана, то принимается текущая дата.
    Список словарей выдается актуальным на эту дату

    Список выдается с pagination = 10"""

    serializer_class = ReferenceSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date', datetime.date(datetime.now()))
        valid_versions = RefVersions.objects.filter(
            init_date__lte=date, reference=OuterRef('pk')).order_by(
            'reference_id', '-init_date').distinct('reference_id')
        reference_list = RefTitles.objects.filter(id__in=valid_versions.values_list('reference', flat=True))
        reference_list_with_version = reference_list.all().values('id', 'name', 'short_name', 'description').annotate(
            version_name=Subquery(valid_versions.values('version')),
            version_id=Subquery(valid_versions.values('id')),
            valid_date=Subquery(valid_versions.values('init_date')))
        return reference_list_with_version


def get_current_version(ref_id):
    date = datetime.date(datetime.now())
    versions = RefVersions.objects.filter(init_date__lte=date, reference_id=ref_id).order_by('-init_date')
    try:
        return versions[0]
    except IndexError:
        return -1


class ElementsAPIView(generics.ListAPIView):
    """ Предоставляет список элментов указанного справочника (по индексу из url).
    В параметрах запроса может указываться номер версии справочника в виде
    ?version=##
    если версия не указана, то берется текущая"""

    serializer_class = ElementsSerializer

    def get_queryset(self):
        ref_id = self.kwargs['pk']
        version = self.request.query_params.get('version', get_current_version(ref_id))
        return Elements.objects.filter(ref_version=version)


class ValidateElementsAPIView(APIView):
    def post(self, request):
        pass