from django import forms
from . import models

class BookstoreCreateForm(forms.ModelForm):

    class Meta:
        model = models.Bookstore
        fields = ['bookstoreName', 'bookstoreExp', 'bookstoreAddress', 'bookstoreTel', 'bookstorePic']
        widgets ={
                "bookstoreName":forms.TextInput(attrs={"class":"form-control"}),
                "bookstoreExp":forms.Textarea(attrs={"class":"form-control"}),
                "bookstoreAddress":forms.TextInput(attrs={"class":"form-control"}),
                "bookstoreTel":forms.TextInput(attrs={"class":"form-control"}),
        }
