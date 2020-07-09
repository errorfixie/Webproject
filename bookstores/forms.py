from django import forms
from . import models

class BookstoreCreateForm(forms.ModelForm):

    class Meta:
        model = models.Bookstore
        fields = "__all__"
        