from django.shortcuts import render
from django.views.generic.list import ListView
from writerblogs import models
from authors.models import Author


class WriterBlogListView(ListView):
    model = models.WriterBlog
    paginate_by = 5
    paginate_orphans = 3
    template_name = "writersblog/writersblog.html"


