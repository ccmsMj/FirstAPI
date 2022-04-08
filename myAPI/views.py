from django.shortcuts import render
from myAPI.models import vehicls
from rest_framework import viewsets
from . serializers import vehiclsSerializer
from . models import vehicls

class vehiclsviewset(viewsets.ModelViewSet):
    quesryset = vehicls.objects.all().order_by('name')
    serializer_class = vehiclsSerializer
# Create your views here.
