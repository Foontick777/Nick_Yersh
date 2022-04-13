from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .form import Form


class GeP(View):
    def get(self, request):
        context = {
            'form': Form(),
            'title': 'Form',
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            print(f'{firstname}, {lastname}, {age}, {comment}')
            return redirect('post')
