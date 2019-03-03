from django.db import models

class Answers(models.Model):
    MONTHS = [
        (1, 'January'),
        (2, 'Febuary'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    ]
    DAYS = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    ]

    fav_month = models.IntegerField(choices=MONTHS)
    fav_day = models.IntegerField(choices=DAYS)