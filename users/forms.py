from .models import User, likebook
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
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
    
    password1 =  forms.CharField(label = '비밀번호', strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =  forms.CharField(label = '비밀번호확인', strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    likebooks = forms.MultipleChoiceField(
                                        label='관심장르', widget = forms.CheckboxSelectMultiple(),
                                        choices = book_choices)
    class Meta:
        model = User
        fields = ['username', 'password1','password2', 'nickName', 'userEmail', 'userAddress', 'userTel', 'writerIntro', 'likebooks', 'userPic']

        widgets ={
                "nickName":forms.TextInput(attrs={"class":"form-control"}),
                "userEmail":forms.EmailInput(attrs={"class":"form-control"}),
                "userAddress":forms.TextInput(attrs={"class":"form-control"}),
                "userTel":forms.TextInput(attrs={"class":"form-control"}),
                "writerIntro":forms.TextInput(attrs={"class":"form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #print(self.cleaned_data['likebooks'])
        if commit:
            user.save()
            for book in self.cleaned_data['likebooks']:
                lb = likebook(userID=user, bookCategoryID=book)
                lb.save()
            
        return user
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label = "회원ID", widget = forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label='비밀번호', strip=False, widget=forms.PasswordInput(attrs={'class':"form-control"}))

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['nickName', 'userEmail', 'userAddress', 'userTel', 'writerIntro']
