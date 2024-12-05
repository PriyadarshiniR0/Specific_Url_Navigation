from django.urls import path
from mall.views import *

app_name='mall'

urlpatterns=[
    path('mic/',mic,name='mic')
]