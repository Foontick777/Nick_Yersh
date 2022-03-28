from django.shortcuts import render
from django.http import HttpResponse
from myapp import *

def Task19_01(request):
    if request.method == "POST":
        result = len(request.POST.get("first_name"))
        str = f"Длина имени = {result} символов"
        return HttpResponse(f"{str}")
    return render(request, "Task19_01.html")


def Task19_03(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        length = len(comment)
        vowels = ["а", "е", "и", "у", "ы", "э", "ю", "я", "о"]
        vowels_count = 0
        consonants_count = 0

        for i in comment:
            if i.lower() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

        str = f"Комментарий = {length} символ(ов). {vowels_count} гласных и "f" {consonants_count} согласных"
        return HttpResponse(f"{str}")
    return render(request, "Task19_03.html")


def Task19_06(request):
    if request.method == "POST":
        name = request.POST.get("first_name")
        nam = {
            "name": name
        }
        return render(request, "Task19_06.html", context=nam)
    return render(request, "Task19_01.html")