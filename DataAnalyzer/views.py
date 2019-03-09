from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
def home(request):
 return render(request,'home.html')
def letanalyze(request):
 return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def analyze(request):
    pjtext = request.POST.get('data', 'default')
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if not djtext.strip():
        messages.add_message(request, messages.INFO, 'Please enter the data')
        return render(request, 'index.html')

    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#&%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                 analyzed=analyzed+char
        params={'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if fullcaps=="on" :
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if spaceremover=="on":
        analyzed=""
        for char in djtext:
            if char!=" ":
                analyzed=analyzed+char
        params = {'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charcount=="on":
        c=0
        for char in djtext:
            c=c+1

        params = {'analyzed_text': c}

        #return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char

        params = {'analyzed_text': analyzed}

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on" and extraspaceremover!="on"):
        messages.add_message(request, messages.INFO, 'Please select any option')
        params = {'analyzed_text': djtext}
        return render(request, 'index.html',params)

    return render(request, 'analyze.html', params)











#def capitalizefirst(request):
    #return HttpResponse("first capitalize")
#def newlineremove(request):
 #   return HttpResponse("remove new lines")
#def charcount(request):
#    return HttpResponse("count the characters")
#def spaceremove(request):
 #   return HttpResponse("remove the spaces")
