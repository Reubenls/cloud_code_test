from django import template

register = template.Library() 

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

@register.filter(name='display_month')
def display_month(value):
    m = dict(MONTHS)
    return m.get(value)

@register.filter(name='display_day')
def display_day(value):
    d = dict(DAYS)
    return d.get(value)

#filter for changing fraction (value/arg) to a percentage
@register.filter(name='as_percentage')
def as_percentage(value, arg):
    p = (value/arg)*100
    p = "{:.2f}%".format(p)
    return p
