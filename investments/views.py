from django.shortcuts import render
from rest_framework import viewsets
from .models import Investment
from .serializers import InvestmentSerializer
# Create your views here.

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
