from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponseRedirect
from .forms import QuestionnaireForm
from .models import Answers


def index(request):
    #TODO: make this a real number:
    num_answers = Answers.objects.count()
    context = {
        'title': "Basic Questions!",
        'num_answers': num_answers,
    }
    return render(request, 'questionnaire/index.html', context)


def questionnaire(request):
    # On POST request process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionnaireForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # save answer to database
            form.save()
            # redirect to a index:
            return HttpResponseRedirect('/')
    # On GET create new form
    else:
        form = QuestionnaireForm()

    return render(request, 'questionnaire/questionnaire.html', {'form': form})

def results(request):
    #count months
    month_count = dict(Answers.objects.values_list('fav_month').annotate(c=Count('fav_month')).order_by('fav_month'))
    
    #count days 
    day_count = dict(Answers.objects.values_list('fav_day').annotate(c=Count('fav_day')).order_by('fav_day'))
    
    #count each month day relation 
    month_day = Answers.objects.values('fav_month','fav_day').annotate(c = Count('fav_day')).order_by('c')
    # days for each month with higer counts will be overwriten due to ordering (low to high) 
    relation_set = {m_d.get('fav_month'):m_d.get('fav_day') for m_d in month_day}
   
    total = Answers.objects.count()
    container = {'month_count':month_count,'day_count':day_count,'relation_set':relation_set, 'total':total}
    
    return render(request, 'questionnaire/results.html', container)
