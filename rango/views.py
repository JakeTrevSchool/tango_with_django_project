from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    CONTEXT_DICT = {"boldmessage":"Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, "rango/index.html", context=CONTEXT_DICT)
    