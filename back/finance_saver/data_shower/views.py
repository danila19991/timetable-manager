from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    context = dict()

    return HttpResponse(template.render(context, request))
