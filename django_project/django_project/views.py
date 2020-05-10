from django.http import HttpResponse
from django.shortcuts import render


#function definitions

def removepunc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    removepunctext=''
    for letter in text:
        if letter not in punctuations:
            removepunctext+=letter
        
    return removepunctext

def capfirst(text):
    cap_text=''
    cap_text=text[0].upper() + text[1:]
    return cap_text

def newlineremove(text):
    newlinetext=''
    for letter in text:
        if letter != '\n' and letter != '\r':
            newlinetext+=letter
    return newlinetext

def spaceremove(text):
    spaceremovetext=''
    for index,letter in enumerate(text):
        if text[index]==' ' and text[index+1]==' ':
            pass
        else:
            spaceremovetext += letter
    return spaceremovetext

def charcount(text):
    counttext=''
    for letter in text:
        if letter != ' ':
            counttext += letter
    count=len(counttext)
    return count

#Home function
def index(request):
    return render(request,'base.html')

def analyze(request):
    removepuncheck=request.POST.get('removepuncheck','off') 
    capcheck=request.POST.get('capcheck','off')
    newlineremovecheck=request.POST.get('newlineremovecheck','off')
    spaceremovecheck=request.POST.get('spaceremovecheck','off')
    charcountcheck=request.POST.get('charcountcheck','off')
    text=request.POST.get('text','default') 
    print(removepuncheck)
    analyzed_text=text
    if removepuncheck=='on':
        analyzed_text=removepunc(analyzed_text)
    
    if capcheck=='on':
        analyzed_text=capfirst(analyzed_text)
    
    if newlineremovecheck=='on':
        analyzed_text=newlineremove(analyzed_text)
        
    
    if spaceremovecheck=='on':
        analyzed_text=spaceremove(analyzed_text)

    if charcountcheck=='on':
        analyzed_text=charcount(analyzed_text)

    dic={
        'analyzed_text':analyzed_text
    }
    return render(request,'analyzed.html',dic)


    
    
    





