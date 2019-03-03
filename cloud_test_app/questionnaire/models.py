from django.db import models

class Answers(models.Model):
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

    fav_month = models.CharField(max_length=3, choices=MONTHS)
    fav_day = models.CharField(max_length=3, choices=DAYS)