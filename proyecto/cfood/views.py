from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *



# Create your views here.




def inicio(request):
    #"C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/templateSusana/index.html"
    total_recipes = Recipe.objects.all().count()
    context = {
        "title": "Homepage",
        "total_recipes": total_recipes,
    }

    return render(request, "C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/home.html", context)


def registerpr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.UserApp.username = form.cleaned_data.get('username')
            user.UserApp.email = form.cleaned_data.get('email')
            user.UserApp.password = form.cleaned_data.get('password')
            user.is_active = True
            user.save()
            print(user)
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = { 'form' : form}
    return render(request,'./register/register.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password'))
            #user.password = form.cleaned_data.get('password')
            user.is_active = True
            user.save()
            print(user)
            return redirect('inicio')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = { 'form' : form}
    return render(request,'./register/register.html', context)



def login2(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        print(username, password, user)
        login(request,user)
        print("usuairo", user)
        return redirect('inicio')
    else:
        form = LoginForm(request.POST)
        context = {'form': form}
        return render(request, 'C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/login.html', context)


"""def login2(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password, user)
        login(request,user)
        print("usuairo", user)
        return redirect('C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/templateSusana/index.html')
    else:
        form = LoginForm(request.POST)
        context = {'form': form}
        return render(request, 'C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/login.html', context)"""



