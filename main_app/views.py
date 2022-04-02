from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.

class Home(TemplateView):#home page, when you sign in you land here
    template_name = "home.html"



class Intro(TemplateView): #intro page that lets you learn about how to use app. may want to switch this to be the landing page later
    template_name = "intro.html"