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
        if password != confirm_password:
            raise serializers.ValidationError(
                'Праоли не совпадают'
            )
        user = User(username=username, email=email, is_active=False)
        user.set_password(password)
        user.save()
        return user

'''class ConfirmEmailSerializer(serializers.ModelSerializer):

    confirm_code = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['conf_code', 'activate', 'confirm_code']
        extra_kwargs = {
            'conf_code' : {'read_only' : True}
        }

    def update(self, instance, validated_data):

        confirm_code = validated_data['confirm_code']

        if len(confirm_code) < 6:
            raise serializers.ValidationError(
                'Код введён не полностью'
            )
        if instance.conf_code != confirm_code:
            raise serializers.ValidationError(
                'Введён неверный код подтверждения'
            )
        instance.activate = True
        instance.save()
        return instance

class ConfirmMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')'''