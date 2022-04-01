from datetime import datetime

from django.db.models import Subquery, OuterRef
from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from references.models import RefVersions, RefTitles
from references.serializers import ReferenceSerializer


# class ReferencesAPIView(APIView):
#     """ Предоставляет ответ на GET запрос со списком словарей
#     в параметрах запроса может указываться дата в формате date = YYY-MM-DD,
#     если дата не указана, то принимается текущая дата.
#     Список словарей выдается актуальным на эту дату
#
#     Список выдается с pagination = 10"""
#
#     # serializer_class = ReferenceSerializer
#
#     def get(self, request):
#         date = self.request.query_params.get('date', datetime.date(datetime.now()))
#         valid_versions = RefVersions.objects.filter(
#             init_date__lte=date, reference=OuterRef('pk')).order_by(
#             'reference_id', '-init_date').distinct('reference_id')
#         reference_list = RefTitles.objects.filter(id__in=valid_versions.values_list('reference', flat=True))
#         ref = reference_list.all().values('id', 'name', 'short_name', 'description').annotate(
#             version_name=Subquery(valid_versions.values('version')),
#             version_id=Subquery(valid_versions.values('id')),
#             valid_date=Subquery(valid_versions.values('init_date')))
#         return Response(ref)

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

class ElementsAPIView(generics.ListAPIView):
    def get_queryset(self):
        ref_id = self.kwargs['pk']
        date = self.request.query_params.get('date', datetime.date(datetime.now()))
        pass
