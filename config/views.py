from django.shortcuts import render
from books import models

# 홈 html 뷰입니다.


def test(request):
    all_books = models.Book.objects.all()
    return render(request, "home/home.html", context={"books": all_books})
