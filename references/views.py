from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from references.models import RefVersions
from references.serializers import ReferenceSerializer


class ReferencesAPIView(generics.ListAPIView):
    queryset = RefVersions.objects.all()
    serializer_class = ReferenceSerializer