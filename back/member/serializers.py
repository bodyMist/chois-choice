from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Members

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password","first_name","last_name","email")

class MemberDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Members
        fields='__all__'