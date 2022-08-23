from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'password', 'confirm_password', 'email', 'conf_code']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']
        email = validated_data['email']
        if password != confirm_password:
            raise serializers.ValidationError(
                'Праоли не совпадают'
            )
        user = Profile(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

class ConfirmEmailSerializer(serializers.ModelSerializer):

    confirm_code = serializers.IntegerField()
    
    class Meta:
        model = Profile
        fields = ['conf_code', 'is_active']

    def update(self, instance, validated_data):

        confirm_code = validated_data['confirm_code']

        if len(confirm_code) < 6:
            raise serializers.ValidationError(
                'Код введён не полностью'
            )
        if instance.conf_code != self.confirm_code:
            raise serializers.ValidationError(
                'Введён неверный код подтверждения'
            )
        instance.is_active = True
        instance.save()
        return instance
