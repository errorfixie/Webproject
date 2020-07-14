from .models import User, likebook
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django import forms

book_choices = [
    ("humanities", "인문"),
    ("sociology", "사회"),
    ("poetry", "시집"),
    ("prose", "산문"),
    ("essay", "수필"),
    ("novel", "소설"),
    ("poem", "시"),
    ("illustration", "삽화"),
]


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        label="회원ID",
        strip=False,
        widget=forms.TextInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )

    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )

    likebooks = forms.MultipleChoiceField(
        label="관심장르",
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "font-medium tracking-wider text-gray-700"}
        ),
        choices=book_choices,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "nickName",
            "userEmail",
            "userAddress",
            "userTel",
            "writerIntro",
            "likebooks",
            "userPic",
        ]

        widgets = {
            "nickName": forms.TextInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "userEmail": forms.EmailInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "userAddress": forms.TextInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "userTel": forms.TextInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "writerIntro": forms.Textarea(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # print(self.cleaned_data['likebooks'])
        if commit:
            user.save()
            for book in self.cleaned_data["likebooks"]:
                lb = likebook(userID=user, bookCategoryID=book)
                lb.save()

        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="회원ID",
        widget=forms.TextInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )
    password = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['nickName', 'userEmail', 'userAddress', 'userTel', 'writerIntro']
