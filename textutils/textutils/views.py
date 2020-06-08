# I have created this file - sarthak


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extspaceremover = request.POST.get('extspaceremover','off')
    purpose = ""

    if removepunc == "on":
        punctuations = r'''!()-[]{};:'",\<>./?@#$%^&*_~'''
        analyzed = "" 
        purpose += "| remove punctuations |"

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : purpose , 'analyzed_text' : analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        purpose += ' | Change to Uppercase |'
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : purpose , 'analyzed_text' : analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        purpose += '| Removed new lines |'
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose' : purpose , 'analyzed_text' : analyzed}
        djtext = analyzed

    if(extspaceremover == "on"):
        analyzed = ""
        purpose += '| Removed Extra spaces |'
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose' : purpose , 'analyzed_text' : analyzed}
    
    if (removepunc == "off" and fullcaps=="off" and newlineremover == "off" and extspaceremover == "off" ):
        return HttpResponse("Please select any operation try again..........!!!!")

    return render(request,'analyze.html',params)


    

