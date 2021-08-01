from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from cocktails.models import Cocktail
from cocktails.models import Measure
from cocktails.models import Ingredient
from cocktails.models import Ingredients


def user_login(request):

    class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            User.objects.get(username=username)
            return HttpResponseRedirect('/cocktails/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_signup(request):

    class SignupForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = User(username=username, password=password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/cocktails/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def my_account(request, id):
    user = User.objects.get(id=id)
    return render(request, 'my_account.html', {'user': user})


def list_cocktails(request):
    return render(request, 'cocktail_list.html', {'cocktails': cocktails})


def view_cocktail(request, id):
    cocktail = Cocktail.objects.get(id=id)
    ingredients = Ingredients.objects.filter(cocktail=id)
    return render(request, 'cocktail_view.html', {'cocktail': cocktail,'ingredients':ingredients})


def confirm_delete_cocktail(request, id):
    cocktail = Cocktail.objects.get(id=id)
    return render(request, 'cocktail_confirm_delete.html', {'cocktail': cocktail})


def delete_cocktail(request, id):
    cocktail = Cocktail.objects.get(id=id).delete()
    return HttpResponseRedirect('/cocktails/')
