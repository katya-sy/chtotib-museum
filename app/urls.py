from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('traditions', TraditionListView.as_view(), name="traditions"),
    path('traditions/<slug:article_slug>', TraditionDetailView.as_view(), name="tradition"),
    path('<slug:slug>', SectionView.as_view(), name="section"),
    path('<slug:slug>/<slug:time_period_slug>', ArticleListView.as_view(), name="article_list"),
    path('<slug:slug>/<slug:time_period_slug>/<slug:article_slug>', ArticleDetailView.as_view(), name="article"),
]
