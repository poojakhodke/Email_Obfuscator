from django import forms
from .models import mailId

class EmailForm(forms.ModelForm):
    class Meta:
        model = mailId
        fields = ('email',)