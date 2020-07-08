from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    # books/
    path('', views.BookList.as_view(), name='list'),
    # books/도서ID/
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
]