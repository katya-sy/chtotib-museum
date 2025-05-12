from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from app.models import *


def index(request):
    context = {
        "sections": [
            {
                "id": 1,
                "title": "История развития",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                               "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
                "icon": "history",
                "url_name": "index"
            },
            {
                "id": 2,
                "title": "Традиции",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                               "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
                "icon": "traditions",
                "url_name": "index"
            },
            {
                "id": 3,
                "title": "Преподаватели",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                               "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
                "icon": "teachers",
                "url_name": "index"
            },
            {
                "id": 4,
                "title": "Выпускники",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                               "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
                "icon": "graduates",
                "url_name": "index"
            },
        ],
        "years": [{"title": "1950-е", "img": "img/banner.jpg"},
                  {"title": "1950-е", "img": "img/banner.jpg"},
                  {"title": "1950-е", "img": "img/banner.jpg"},
                  {"title": "1950-е", "img": "img/banner.jpg"},
                  {"title": "1950-е", "img": "img/banner.jpg"},
                  {"title": "1950-е", "img": "img/banner.jpg"},
                  {"title": "1950-е", "img": "img/banner.jpg"},
                  ],
        "articles": [{"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/test.png"},
                     {"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/banner.jpg"},
                     {"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/banner.jpg"},
                     {"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/banner.jpg"},
                     {"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/test.png"},
                     {"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/test.png"},
                     {"title": "Статья",
                      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. ",
                      "url_name": "index", "img": "img/banner.jpg"},
                     ],
        "images": [
            "img/test.png", "img/banner.jpg", "img/test.png", "img/banner.jpg", "img/banner.jpg", "img/test.png",
            "img/banner.jpg",
        ]
    }

    return render(request, 'pages/article.html', context)


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
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'pages/article.html'
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'


class TraditionListView(ListView):
    model = Tradition
    template_name = 'pages/traditions.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = Section.objects.get(slug="traditions")
        return context


class TraditionDetailView(DetailView):
    model = Tradition
    template_name = 'pages/article.html'
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'
