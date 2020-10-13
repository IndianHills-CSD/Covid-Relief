from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
 
def home(request):
    dummy = {'Active': 28, 'Recovered': 31, 'Uninfected': 62}
    #return HttpResponse('<h1>hello</h1>')
    return render(request, 'loginApp/home.html',dummy)


def login(request):
    #return HttpResponse('<h1>login</h1>')
    return render(request, 'loginApp/login.html')

def register(request):
    #return HttpResponse('<h1>register</h1>')
    return render(request, 'loginApp/register.html')

