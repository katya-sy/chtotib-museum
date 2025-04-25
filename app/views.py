from django.shortcuts import render
from django.views.generic import TemplateView

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
