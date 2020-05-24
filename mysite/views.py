# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #GET THE TEXT
    djtext = request.GET.get('text', 'default')
    #CHECK CHECKBOX VALUES
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    smallcaps = request.GET.get('smallcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    exstraspaceremover = request.GET.get('exstraspaceremover', 'off')
    #CHECK WHICH CHECKBOX IS ON
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations', 'analyze_text': analyzed}
        return render(request, 'analyze.html' , params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change it to Uppercase', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (smallcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Change it to LowerCase', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (exstraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):

                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)






    else:
        return HttpResponse("Error")


#def capfirst(request):
 #   return HttpResponse("capitalize first")

#def newlineremove(request):
   # return HttpResponse("newline remove first")


 #def spaceremove(request):
    #return HttpResponse("space remover back")