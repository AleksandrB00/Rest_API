from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']
        email = validated_data['email']
        
