from django.http import HttpResponse
from django.template import loader

from .models import Cases

def index(request):
    cases_list = Cases.objects.all()
    template = loader.get_template('countrycases/index.html')
    context = {
        'cases_list': cases_list
    }
    return HttpResponse(template.render(context, request))