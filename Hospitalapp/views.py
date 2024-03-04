from django.shortcuts import render, redirect
from Hospitalapp.models import Member, Contact, Users,ImageModel
from Hospitalapp.forms import ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        contacts = Contact(name=request.POST['name'],
                           email=request.POST['email'],
                           subject=request.POST['subject'],
                           message=request.POST['message'])
        contacts.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        member = Member(Username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'Register.html')


def login(request):
    return render(request, 'Login.html')





def detail(request):
    details = Contact.objects.all()
    return render(request, 'details.html', {'details': details})


def user(request):
    users = Users.objects.all()
    return render(request, 'user.html', {'user': users})

def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(Username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(Username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')