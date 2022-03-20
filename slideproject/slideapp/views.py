from django.shortcuts import render
from django.http import HttpResponse

def slide(request):
    return render(request,'slide.html')

