from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.htm')

def content(request):
    if request.method=="POST":
        return render(request,'content.htm')
    return HttpResponse('abhi reset karke deta hu')

def signup(request):
    if request.method=="POST":
        return HttpResponse('done submitted go back and login again')
    return render(request,'signup.htm')

def something(request):
    if request.method=="POST":
        if request.POST.get('com'):
            a=[]
            for i in range(7):
                a.append(i)
                    
            
            return render(request,'something.htm',{'range':a,'key':'com'})
        elif request.POST.get('sig'):
            a=[]
            for i in range(73):
                a.append([i+1,i])
            return render(request,'something.htm',{'range':a,'key':'sig'})
        elif request.POST.get('net'):
            a=[]
            for i in range(192):
                a.append([i+1,i])
            return render(request,'something.htm',{'range':a,'key':'net'})
        elif request.POST.get('ana'):
            a=[]
            for i in range(78):
                a.append([i+1,i])
            return render(request,'something.htm',{'range':a,'key':'ana'})
        
    return HttpResponse('failed')
def studyM(request):
    if request.method=="POST":
        if request.POST.get('ecstd'):
            key='ec'
            return render(request,"studyM.htm",{'key':key})