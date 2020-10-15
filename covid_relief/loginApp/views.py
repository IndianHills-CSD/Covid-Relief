from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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
    return render(request, 'loginApp/register.html')

