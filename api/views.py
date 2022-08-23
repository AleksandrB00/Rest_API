from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.core.mail import send_mail


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return Response({
            'message' : 'Пользователь успешно создан'
        })

class ConfirmEmailView(generics.GenericAPIView):
    serializer_class = ConfirmEmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message' : 'Email успешно подтверждён'
        })

'''class SendConfirmMailView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConfirmMailSerializer

    def get(self, request):
        email = request.user.email
        send_mail('Код подтверждения', f'здравствуйте {request.user.username}, ваш код потверждения - {request.user.profile.conf_code}','', [email])
        return Response({
            'message' : 'Код подтверждения отправлен'
         })'''