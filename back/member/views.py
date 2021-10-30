from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import MemberSerializer
from .models import Members

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Members.objects.all()

class DetailMember(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Members.objects.all()

# Create your views here.
