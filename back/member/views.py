from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Members

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Members.objects.all()

# Create your views here.
