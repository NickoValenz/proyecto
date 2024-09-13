from django.shortcuts import render

# Create your views here.

def inicioPeli(request):
    return render(request,"aplicacion/inicioPeli.html")

def verPeli1(request):
    return render(request, "aplicacion/verPeli1.html")

def verPeli2(request):
    return render(request, "aplicacion/verPeli2.html")

def verPeli3(request):
    return render(request, "aplicacion/verPeli3.html")