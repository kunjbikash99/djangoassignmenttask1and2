from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'myapp/login.html')

def cong(request):
    return HttpResponse("Congratulations!you have signed in")