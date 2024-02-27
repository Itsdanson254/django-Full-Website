from django.shortcuts import render,redirect
from Hospitalapp.models import Member,details
# Create your views here.
def index (request):
    if request.method == 'POST':
        member = details(fullname=request.POST['name'], email=request.POST['email'],subject=request.POST['subject'], message =request.POST['message'])
        member.save()
        return redirect('/index')
    else:
        return render(request, 'index.html')


def inner (request):
    return render(request, 'inner-page.html')



def register (request):
    if request.method == 'POST':
        member = Member(Username=request.POST['username'],email=request.POST['email'], password=request.POST['password'])
        member.save()
        return redirect('/register')
    else:
        return render(request, 'Register.html')




def login  (request):
    return render(request, 'Login.html')

def upload  (request):
    return render(request, 'upload.html')