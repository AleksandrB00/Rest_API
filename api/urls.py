from .views import *
from django.urls import path


urlpatterns =[
   path('signup/', SignUpView.as_view()),
   path('conf_mail/', ConfirmEmailView.as_view()) 
]