from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuestionnaireForm

def index(request):
    #TODO: make this a real number:
    num_answers = 0
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
            # TODO: process the data in form.cleaned_data as required
            
            # redirect to a index:
            return HttpResponseRedirect('/')
    # On GET create new form
    else:
        form = QuestionnaireForm()

    return render(request, 'questionnaire/questionnaire.html', {'form': form})
