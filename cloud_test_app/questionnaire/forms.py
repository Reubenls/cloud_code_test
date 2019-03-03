from django import forms
from .models import Answers

class QuestionnaireForm(forms.ModelForm):
   
    class Meta:
        model = Answers
        fields = ['fav_month', 'fav_day']
        labels = {
            "fav_month": "What is your favourite month?",
            "fav_day": "What is your favourite day?"
        }