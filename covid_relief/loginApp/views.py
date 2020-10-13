from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
 
 
def home(request):
    
    context = {
    	'userInfo': Post.objects.all()
    }
    return render(request, 'loginApp/home.html',context)


def login(request):
    return HttpResponse('<h1>login</h1>')

def register(request):
    return HttpResponse('<h1>register</h1>')

