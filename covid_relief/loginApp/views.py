from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import UserRegisterForm
# Create your views here.
 
 
def home(request):
    
    context = {
    	'Posts': Post.objects.all()
    }
    return render(request, 'loginApp/home.html',context)


def login(request):
    #return HttpResponse('<h1>login</h1>')
    return render(request, 'loginApp/login.html')

def register(request):
    #return HttpResponse('<h1>register</h1>')
    if request.method == 'POST':
    	form = UserRegisterForm(request.POST)
    	if form.is_valid():
    		form.save()
    		username = form.cleaned_data.get('username')
    		return redirect('home')
    else:
    	form = UserRegisterForm()
    return render(request, 'loginApp/register.html', {'form': form })
