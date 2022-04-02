from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class DamirPageView(TemplateView):
    template_name = 'Damir.html'


def method(requst):
    return HttpResponse('mana metod')

class BasePageView(TemplateView):
    template_name = 'base.html'