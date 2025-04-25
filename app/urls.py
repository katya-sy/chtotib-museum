from django.urls import path

from .views import *

urlpatterns = [
    path('index', index, name='df'),
    path('indexq', index, name='history'),
    path('indexd', index, name='teachers'),
    path('indexdfv', index, name='graduates'),
    path('indexdfv', index, name='traditions'),
    path('', MainPageView.as_view(), name='index'),
]
