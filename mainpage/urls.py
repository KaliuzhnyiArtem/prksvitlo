from django.urls import path

from mainpage.views import *


urlpatterns = [
    path('', homepage),
]