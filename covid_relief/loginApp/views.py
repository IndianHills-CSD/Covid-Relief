from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .models import UserInfo
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
    errmsg = ''
    if request.method == 'POST':
    	form = UserRegisterForm(request.POST)
    	address = request.POST.get('address')
    	
    	if (form.is_valid() and request.POST.get('address') != ''):
    		form.save()
    		username = form.cleaned_data.get('username')
    		ui = UserInfo(address=request.POST.get('address'),status=request.POST.get('status'),userKey=username)
    		ui.save()
    		return redirect('home')
    	else:
    		if request.POST.get('address') == '':
    			errmsg = "must enter an address"
    		else:
    			errmsg = ''
    else:
    	form = UserRegisterForm()
    	
    return render(request, 'loginApp/register.html', {'form': form, 'err' : errmsg})
