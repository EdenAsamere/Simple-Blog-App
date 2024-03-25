from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse('hELLO ABOUT')
    return render(request,'about.html')


def home(request):
    # return HttpResponse('Home sweet home')
    return render(request,'home.html')
    