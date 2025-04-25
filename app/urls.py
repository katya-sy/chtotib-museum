from django.urls import path

from .views import *

urlpatterns = [
    path('index', index, name='df'),
    path('indexd', index, name='teachers'),
    path('indexdfv', index, name='graduates'),
    path('indexdfv', index, name='traditions'),
    path('', MainPageView.as_view(), name='index'),
    path('section/<slug:slug>', SectionView.as_view(), name="section"),
]
