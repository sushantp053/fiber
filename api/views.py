from django.shortcuts import render
from home.models import *
from rest_framework import viewsets
from api.serializers import *


# Create your views here.


class NatoshiViewSet(viewsets.ModelViewSet):

    queryset = Natoshi.objects.all()
    serializer_class = NatoshiSerializer
