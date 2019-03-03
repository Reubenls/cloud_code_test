from django import forms
from .models import Answers

class QuestionnaireForm(forms.ModelForm):
   
    class Meta:
        model = Answers
        fields = ['fav_month', 'fav_day']