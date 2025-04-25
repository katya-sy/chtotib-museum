from django.urls import path

from .views import *

urlpatterns = [
    path('index', index, name='df'),
    path('indexd', index, name='teachers'),
    path('indexdfv', index, name='graduates'),
    path('indexdfv', index, name='traditions'),
    path('', MainPageView.as_view(), name='index'),
    path('<slug:slug>', SectionView.as_view(), name="section"),
    path('<slug:slug>/<slug:time_period_slug>', ArticleListView.as_view(), name="article_list"),
    path('<slug:slug>/<slug:time_period_slug>/<slug:article_slug>', ArticleDetailView.as_view(), name="article"),
]
