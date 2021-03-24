from django import forms
from testApp.models import Comments
class comment_form(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')
