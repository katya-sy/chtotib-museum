from django.shortcuts import render


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


