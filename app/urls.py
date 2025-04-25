from django.urls import path

from .views import *

urlpatterns = [
    path('index', index, name='df'),
    path('', MainPageView.as_view(), name='index'),
]
