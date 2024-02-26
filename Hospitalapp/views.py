from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')

def inner (request):
    return render(request, 'inner-page.html')

def register (request):
    return render(request, 'Register.html')

def login  (request):
    return render(request, 'Login.html')