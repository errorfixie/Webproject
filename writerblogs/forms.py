from django import forms
from . import models

class writersblogCreateForm(forms.ModelForm):

    class Meta:
        model = models.WriterBlog
        exclude = ['userID']
    