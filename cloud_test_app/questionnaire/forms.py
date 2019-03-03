from django import forms

class QuestionnaireForm(forms.Form):
    MONTHS = (
        ('JAN', 'January'),
        ('FEB', 'Febuary'),
        ('MAR', 'March'),
        ('APR', 'April'),
        ('MAY', 'May'),
        ('JUN', 'June'),
        ('JUL', 'July'),
        ('AUG', 'August'),
        ('SEP', 'September'),
        ('OCT', 'October'),
        ('NOV', 'November'),
        ('DEC', 'December')
    )
    DAYS = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )
    fav_month = forms.ChoiceField(label='My Favourite Month', choices=MONTHS)
    fav_day = forms.ChoiceField(label='My Favourite Day', choices=DAYS)