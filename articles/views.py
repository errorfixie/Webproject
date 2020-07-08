from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
from datetime import datetime


# 이달의 도서 
# 필요 요소: 도서 사진, 기사 제목, 기사 내용, 등록일자, 도서카테고리, 기사카테고리
# 기능 : 기사카테고리 드롭박스, 페이지네이션, 도서카테고리 박스 - 카테고리 별 filter, 등록일자 년 박스, 등록일자 월 박스
def ThisMonthBookView(request): 
    book_info_date_year = []
    book_info_date_month = []
    book_info = Article.objects.filter(articleCategory="book").order_by('articleDate')

    for i in book_info:
        year = i.articleDate.year
        month = i.articleDate.month
        book_info_date_year.append(year)
        book_info_date_month.append(month)

    book_info_date_year = set(book_info_date_year)
    book_info_date_month = set(book_info_date_month)

    if request.GET.get('cate_year'):
        page_year = request.GET.get('cate_year')
        book_info = Article.objects.filter(articleCategory="book",articleDate__year=page_year)
    elif request.GET.get('cate_month'):
        page_month = request.GET.get('cate_month')
        book_info = Article.objects.filter(articleCategory="book",articleDate__month=page_month)
    
    paginator = Paginator(book_info, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"articles/book.html",{"page_obj":page_obj,"book_info_date_year":book_info_date_year,"book_info_date_month":book_info_date_month})
# 이달의 행사
# 필요 요소: 행사사진, 행사 이름, 기사 내용, 등록일자, 기사카테고리 
# 기능 : 기사카테고리 드롭박스, 검색도구, 페이지네이션
# pagination
def ThisMonthEventView(request):
    event_info = Article.objects.filter(articleCategory="event")
    paginator = Paginator(event_info, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # return render(request,"articles/event.html",{"event_info":event_info, "page_obj":page_obj})
    return render(request,"articles/event.html",{"page_obj":page_obj})
# 검색도구
def result(request):
    query = request.GET['query']
    posts = None
    if query:
        posts = Article.objects.all().filter(articleTitle__contains=query,articleCategory="event")
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"articles/result.html",{"page_obj":page_obj})

# 이달의 작가 
# 필요 요소: 행사 사진, 작가사진, 작가등등 작가Id, 기사제목, 기사내용, 기사카테고리 
# 기능 : 기사카테고리 드롭박스
def ThisMonthAuthorView(request):
    author_info = Article.objects.filter(articleCategory="author")[:1]
    return render(request,"articles/author.html",{"author_info":author_info},)
