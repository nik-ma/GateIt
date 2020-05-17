from django.shortcuts import render,redirect
from django.http import HttpResponse
import re
from random import *
from . import models
from .models import viewers
from django.contrib import messages
from django.contrib.auth.models import User,auth
from datetime import date
from django.core.mail import send_mail


OTP = int(random()*10000)
dict = {'com':'\communication','sig': '\signal','net': '\etwork','dig':'\DigitalE','ana':'\AnalogE','emf':'\emft','cos':'\control',
'sigE':'\signal','elm':'\electricMachines','digE':'\DigitalE','math':'engineering_mathematics','digl':'\Digitallogic','coa':'\COA',
'ds':'\ProgrammingDS','alg':'\Algorithm','toc':'\Toc','cod':'\CompilerD','os':'\OperatingS',
'data':'\DBMS','con':'\ComputerN','em':'\EngineeringM','vbr':'\Vibrations','tom':'\Theory_of_machines','pde':'\productionEngineering',
'tmd':'\Thermodynamics','emc':'\engineeringMechanics','flm':'\Fluid_mechanics',
'ind':'\industrialEngineering','mcd':'\machineDesign','het':'\heat_transfer','mtr':'\materials','mfe':'\manufacturing_engineering',
'cmm':'\construction_materials_and_management','fldc':'\Fluid_mechanicsC','gte':'\geotechnical_engineering','enve':'\environmental_engineering',
'cons':'\concrete_structures','emcc':'\engineering_mechanicsC','hdr':'\hydrology','sdm':'\solid_mechanics',
'sts':'\steel_structures','tre':'\Transportation_engineering','eim':'\electrical_im','pws':'\Power_system',
'nmbt':'\Mumber_theory','dym':'\dynamic_p','gpht':'\Graph_theory'

}


def home(request):
    if request.user.is_authenticated:
        return redirect('content')
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        if User.objects.filter(email=email).exists():

            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username,password=password)
            if user:
                auth.login(request,user)
                key = 'Hello '+user.username
                key2 = 12
                return redirect('content')
            else:
                messages.info(request,'Invalid username Or password')
                return redirect('/')
        else:
            messages.info(request,'Invalid username Or password')
            return redirect('/')

    return render(request,'home.htm')
def logout(request):
    auth.logout(request)
    return redirect('/')

def content(request):
    key ='Hello ' +request.user.username
    return render(request,'content.htm',{'key':key,'key2':12}) 
def guestContent(request):
    key = 'Hello '+'Guest'
    return render(request,'content.htm',{'key':key}) 

    

def signup(request):
    if request.method=="POST":
        global name
        name = request.POST.get('name')
        global email
        email = request.POST.get('email')
        global password
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists ')
                return redirect('signup')
            elif User.objects.filter(username=name).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            else:
                send_mail('Hello from nikhil',' your otp for verifying your email '+str(OTP),'physiotherapyrupam@gmail.com',[email ],fail_silently=False)
                send_mail('Users',name+'  requested for otp and his email is :'+ email,'physiotherapyrupam@gmail.com',['nikhilmaurya5618056@gmail.com'],fail_silently=False)
                return render(request,'reset.htm',{'key':'true'}) 
        else:
            messages.info(request,'Passwords Not Matched')
            return redirect('signup')
        

             
    return render(request,'signup.htm')

def ecContent(request):
    if request.method=="POST":
        key = request.POST.get('btn')
        value = dict[str(key)]
        myfile=open(r'C:\Users\Nikhil\Desktop\GATEweb\gateweb\files'+value+'.txt','r+')
        a=myfile.readlines()
        new=[x[:-1] for x in a ]
        b=[]
        for i in range(0,len(new),2):
            b.append([new[i],new[i+1]])
        return render(request,'ecContent.htm',{'data': b,'key':str(key)})
           
        
    return HttpResponse('failed')
def studyM(request):
    if request.method=="POST":
        key = request.POST.get('btn')
        key = str(key)
        if key == 'ecstd':
            return render(request,'studyM.htm')
        elif key == 'csstd':
            return render(request,'csstd.htm')
        elif key == 'eestd':
            return render(request,'eestd.htm')
        elif key == 'mestd':
            return render(request,'mestd.htm')
        elif key == 'cestd':
            return render(request,'cestd.htm')
        elif key == 'mmstd':
            return render(request,'mmstd.htm')

    return HttpResponse('ertdfgfg')
def about(request):
    if request.method  == "POST":
        return render(request,'about.htm')
    return render(request,'about.htm')
        
def search(request):
    if request.method == "POST":
        sobj = request.POST.get('sea')
        sobj = sobj.lower() 
        value = request.POST.get('btn')
        key=str(value)
        value=dict[str(value)]
        myfile=open(r'C:\Users\Nikhil\Desktop\GATEweb\gateweb\files'+value+'.txt','r+')
        a=myfile.readlines()
        new=[x[:-1] for x in a ]
        new1=[x.lower() for x in new]
        l=list(filter(lambda x: sobj in x, new1))
        if sobj=="":
            b=[]
            for i in range(0,len(new),2):
                b.append([new[i],new[i+1]])
            return render(request,'ecContent.htm',{'data':b,'key':key})
        b=[]
        for i in l:
            k=new1.index(i)
            if k%2==0:
                b.append([new[k],new[k+1]])
       
        if len(b)==0:
            return HttpResponse('no search reslutls')
        else:
            return render(request,'ecContent.htm',{'data':b,'key':key})
def reset2(request):
    if request.method=="POST":
        otpe=request.POST.get('otpe')
        if int(otpe)==OTP:
            user = User.objects.create_user(name,email,password)
            user.save()
            return redirect('home')
        else:  
            return HttpResponse('wrong otp')
    return render(request,'reset.htm',{'key':'true'})

    
