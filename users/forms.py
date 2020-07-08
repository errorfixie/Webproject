from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class CreateUserForm(UserCreationForm):

    userPW =  forms.CharField(label = '비밀번호', strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        field = [ID, userPW, nickName, userEmail, userAddress, userTel, writerIntro, userPic]]
        widgets ={
                "ID":forms.TextInput(attrs={"class":"form-control"})
                "nickName":forms.TextInput(attrs={"class":"form-control"})
                "userEmail":forms.EmailInput(attrs={"class":"form-control"})
                "userAddress":forms.TextInput(attrs={"class":"form-control"})
                "userTel":forms.TextInput(attrs={"class":"form-control"})
                "writerIntro":forms.TextInput(attrs={"class":"form-control"})
        }

    def clean(self):
        cleaned_data = super().clean()
        ID = cleaned_data.get('ID')
        nickName = cleaned_data.get('nickName')
        userEmail = cleaned_data.get('userEmail')
        userAddress = cleaned_data.get('userAddress')
        userTel = cleaned_data.get('userTel')
        writerIntro = cleaned_data.get('WriterIntro')

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
class ItemForm(forms.Form):
    likebooks = forms.MultipleChoiceField(choices = book_choices)
        
class UserLoginForm(AuthenticationForm):
    ID = Forms.CharField(label = "회원ID", widget = forms.TextInput(attrs={'class':"form-control"}))
    userPW = forms.CharField(label='비밀번호', strip=False, widget=forms.PasswordInput(attrs={'class':"form=control"}))

class CustomUserChangeForm(UserChangeform):
    class Meta:
        model = get_user_model()
        fields = ['nickName', 'userEmail', 'userAddress'. 'userTel', 'writerIntro']
