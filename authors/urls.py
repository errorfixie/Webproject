from django.urls import path
from authors import views


urlpatterns = [
    path("<int:pk>/", views.author, name="author"),
]
