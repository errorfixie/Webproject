from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# 로그인 인증 decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Bookstore
from .forms import BookstoreCreateForm

# 서점 목록
class BookstoreListView(ListView):
    model = Bookstore
    template_name = 'bookstores/list.html'
    context_object_name = 'bookstore_list'
    # paginate_by = 5

# 서점 상세보기
class BookstoreDetailView(DetailView):
    model = Bookstore
    template_name = 'bookstores/detail.html'
    context_object_name = 'bookstore_detail'

# 서점 등록
# @method_decorator(login_required, name='dispatch')
class BookstoreCreateView(CreateView):
    form_class = BookstoreCreateForm
    template_name = 'bookstores/create.html'

    def get_success_url(self):
        return reverse('bookstores:detail', args=[self.object.pk])

# 서점 수정
# @method_decorator(login_required, name='dispatch')
class BookstoreUpdateView(UpdateView):
    form_class = BookstoreCreateForm
    template_name = 'bookstores/update.html'
    model = Bookstore

    def get_success_url(self):
        return reverse('bookstores:detail', args=[self.object.pk])

# 서점 삭제
# @login_required
def bookstore_delete(request, pk):
    bookstore = Bookstore.objects.get(pk=pk)
    bookstore.delete()
    return redirect('bookstores:list')
