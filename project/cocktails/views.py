from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect

from cocktails.models import Cocktail
from cocktails.models import Measure
from cocktails.models import Ingredient
from cocktails.models import Ingredients

import itertools
import random

@csrf_protect
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
    cocktails_list = Cocktail.objects.only('image','id','name')
    paginator = Paginator(cocktails_list,12)
    page = request.GET.get('page', 1)
    try:
        cocktails = paginator.page(page)
    except PageNotAnInteger:
        cocktails = paginator.page(1)
    except EmptyPage:
        cocktails = paginator.page(paginator.num_pages)
    return render(request, 'cocktail_list.html', {'cocktails': cocktails})


def view_cocktail(request, id):
    cocktail = Cocktail.objects.get(id=id)
    ingredients = Ingredients.objects.filter(cocktail=id)
    similar_cocktails = Cocktail.objects.filter(category=cocktail.category.id)
    similar_cocktails_list = list(similar_cocktails)
    random_list = random.choices(similar_cocktails_list,k=3)
    return render(request, 'cocktail_view.html', {'cocktail': cocktail,'ingredients':ingredients,'random_list':random_list})

class DeleteForm(forms.Form):
    id = forms.CharField()

@csrf_protect
def confirm_delete_cocktail(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            id = form.data['id']
            cocktail = Cocktail.objects.get(id=id)
            return render(request, 'cocktail_confirm_delete.html', {'cocktail': cocktail})

@csrf_protect
def delete_cocktail(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            id = form.data['id']
            cocktail = Cocktail.objects.get(id=id).delete()
    return HttpResponseRedirect('/cocktails/')

