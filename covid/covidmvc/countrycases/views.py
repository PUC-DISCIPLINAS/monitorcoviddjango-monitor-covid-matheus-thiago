from django.shortcuts import render

from .models import Cases

def index(request):
    cases_list = Cases.objects.order_by('-confirmed_cases')
    context = {
        'cases_list': cases_list
    }
    return render(request, 'countrycases/index.html', context)