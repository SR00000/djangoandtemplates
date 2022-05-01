from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My Second Project!</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'django_app2/help.html',context=helpdict)

# Create your views here.
