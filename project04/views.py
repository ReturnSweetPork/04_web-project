from django.shortcuts import render,redirect

# Create your views here.
def start(request):
    return render(request,"movie/start.html")
    