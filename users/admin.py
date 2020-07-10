from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm
from .models import User

# class CustomUserAdmin(UserAdmin):
#     form = CreateUserForm

    

admin.site.register(User)
