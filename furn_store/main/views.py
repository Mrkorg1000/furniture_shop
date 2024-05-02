from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.


def index(request: any) -> HttpResponse:

    

    context: dict[str, str] = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, 'main/index.html', context)


def about(request: any) -> HttpResponse:
    context: dict[str, str] = {
        "title": "Home - О Нас",
        "content": "О Нас",
        "text_on_page": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }
    return render(request, "main/about.html", context)
