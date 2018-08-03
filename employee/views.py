from django.shortcuts import render
from rest_framework import viewsets
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=User.objects.all();

# Create your views here.
