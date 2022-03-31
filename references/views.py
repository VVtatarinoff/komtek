from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.views import APIView

from references.models import RefVersions
from references.serializers import ReferenceSerializer


class ReferencesAPIView(generics.ListAPIView):
    serializer_class = ReferenceSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date', datetime.date(datetime.now()))
        return RefVersions.objects.filter(
            init_date__lte=date).order_by('reference_id', '-init_date').distinct('reference_id')


