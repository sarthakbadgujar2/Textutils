# I have created this file - sarthak


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    djtext = request.GET.get('text','default')
    return HttpResponse("remove punc <br> <a href='/'> back to index </a>")

def capfirst(request):
    return HttpResponse("capitalize First")

def newlineremove(request):
    return HttpResponse("New Line remove")

def spaceremove(request):
    return HttpResponse("Space remove")

def charcount(request):
    return HttpResponse("Character counter")

