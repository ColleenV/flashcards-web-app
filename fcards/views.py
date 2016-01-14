from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CardForm, SetForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Subject, Card



# Create your views here.
def index(request):
    return HttpResponse("Yay")

def main(request):
    cards = Card.objects.order_by('created')
    sets = Subject.objects.filter(user=request.user.profile)

    return render(request,
                  'fcards/index.html',
                  {'cards': cards, 'sets':sets})

def register(request):
    registered = False    
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            registered = True
        
        else:
            print user_form.errors

    else:
        user_form = UserForm()
        
    return render(request,
                  'fcards/register.html',
                  {'user_form':user_form, 'registered':registered})
        

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return HttpResponseRedirect('/fcards/')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login information.")
        
    else:
        return render(request,'fcards/login.html', {})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/fcards/')
        
def card_new(request):
    
    if request.method == 'POST':
        sform = SetForm(request.POST)
        form = CardForm(request.POST)
        
        if form.is_valid() and sform.is_valid():

            sub = sform.save(commit=False)
            sub.user = request.user.profile
            sub.save()
            
            car = form.save(commit=False)
            car.card = sub 
            car.save()
            
            return HttpResponseRedirect('/fcards/')

        
    else:
        form = CardForm()
        sform = SetForm()
        
    return render(request, 'fcards/create_term.html', 
                  {'sform':sform, 'form':form})
    
def list_set(request):
    sets = Subject.objects.all()
    return sets

def list_card(request, pk):
    cards = Card.objects.filter(card=pk).order_by('created')
    return cards