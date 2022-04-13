from django.shortcuts import render, redirect
from .form import Form
from .models import Customer


def home(request):
    return render(request, 'home.html')


def form(request):
    if request.method == 'GET':
        context = {
            'form': Form(),
        }
        return render(request, 'form.html', context)
    elif request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            return redirect('form')
