from django.urls import path
from writerblogs.views import WriterBlogListView


urlpatterns = [
    path("<int:pk>/", WriterBlogListView.as_view(), name="writerblog"),
]
