from django.shortcuts import redirect, render
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from .models import PsgPredictor,Result
from django.contrib import messages
from .forms import PredictionForm,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import pickle
import numpy as np

def predictor(request):
    a = PredictionForm()

    with open('psg.pickle', 'rb') as f:
        mode = pickle.load(f)

    if request.method == "POST":
        print(request.POST)
        a = PredictionForm(request.POST)

        comp = request.POST.get('competition')
        day =  request.POST.get('day')
        venue =  request.POST.get('venue')
        opponent =  request.POST.get('opponent')
        captain =  request.POST.get('captain')
        formation =  request.POST.get('formation')

        values = np.array([comp,day,venue,opponent,captain,formation]).reshape(1, -1)

        res = mode.predict(values)

        c = ''

        if comp == 3:
            c += 'PSG Champions League match'
        elif comp == 2:
            c += 'PSG League 1 match'
        elif comp == 1:
            c += 'PSG Coup de France'

        Result.objects.create(competition = c, win_or_lose = res)

        if a.is_valid():
            a.save()
        return redirect('database')

    return render(request,'predictor/predictor.html', {'a' : a})

def database(request):
    result = Result.objects.all()
    return render(request,'predictor/database.html', {'result':result})

def prediction(request, pk):
    a = Result.objects.get(id=pk)

    return render(request,'predictor/prediction.html',{'a':a})

def delete(request,pk):
    result = Result.objects.get(id=pk)
    result.delete()
    return redirect('database')

def signup(request):
    a = UserForm()
    if request.method == 'POST':
        a = UserForm(request.POST)
        if a.is_valid():
            a.save
        return redirect(loginPage)

    return render(request, 'predictor/signup.html', {'a':a})

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username, password= password)
        except:
            messages.error(request,"Password or Username is incorrect")
        
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")

    return render(request,'predictor/loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

