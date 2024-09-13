from django import forms
from .models import GamingYoutuber

class GamingYoutuberForm(forms.ModelForm):
    class Meta:
        model = GamingYoutuber
        fields = ['name', 'department', 'salary', 'phone_number']