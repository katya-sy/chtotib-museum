from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from app.models import *
from app.utils.breadcrumbs import get_breadcrumbs


class MainPageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['main_page_content'] = MainPageContent.objects.get(pk=1)
        except MainPageContent.DoesNotExist:
            context['main_page_content'] = {
                "title": "Добро пожаловать в музей ЧТОТиБ!",
                "description": "Стены нашего техникума хранят обширную историю людей...",
            }
        context['sections'] = Section.objects.all()
        return context


class SectionView(TemplateView):
    template_name = 'pages/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = Section.objects.get(slug=kwargs['slug'])
        context['time_periods'] = TimePeriod.objects.all().order_by("start_year")

        path = self.request.path

        parts = [p for p in path.split('/') if p]

        model_by_index = {
            0: Section
        }

        context['breadcrumbs'] = get_breadcrumbs(model_by_index, parts)
        context['path'] = path
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'pages/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        time_period_slug = self.kwargs.get('time_period_slug')
        section_slug = self.kwargs.get('slug')
        return Article.objects.filter(section__slug=section_slug, time_period__slug=time_period_slug)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = Section.objects.get(slug=self.kwargs.get('slug'))
        context['time_period'] = TimePeriod.objects.get(slug=self.kwargs.get('time_period_slug'))

        path = self.request.path

        parts = [p for p in path.split('/') if p]

        model_by_index = {
            0: Section,
            1: TimePeriod
        }

        context['breadcrumbs'] = get_breadcrumbs(model_by_index, parts)
        context['path'] = path
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'pages/article.html'
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path

        parts = [p for p in path.split('/') if p]

        model_by_index = {
            0: Section,
            1: TimePeriod,
            2: Article
        }

        context['breadcrumbs'] = get_breadcrumbs(model_by_index, parts)
        context['path'] = path
        return context


class TraditionListView(ListView):
    model = Tradition
    template_name = 'pages/traditions.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = Section.objects.get(slug="traditions")

        path = self.request.path

        parts = [p for p in path.split('/') if p]

        model_by_index = {
            0: Section
        }

        context['breadcrumbs'] = get_breadcrumbs(model_by_index, parts)
        context['path'] = path
        return context


class TraditionDetailView(DetailView):
    model = Tradition
    template_name = 'pages/tradition.html'
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path

        parts = [p for p in path.split('/') if p]

        model_by_index = {
            0: Section,
            1: Tradition
        }

        context['breadcrumbs'] = get_breadcrumbs(model_by_index, parts)
        context['path'] = path
        return context
