from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
from .models import UserInfo
from django.views.generic import CreateView
from .forms import UserRegisterForm
# Create your views here.

 
def home(request):
    all = UserInfo.objects.all()
    i = UserInfo.objects.filter(status='infected')
    iLen = len(i)
    u = UserInfo.objects.filter(status='uninfected')
    uLen = len(u)
    r = UserInfo.objects.filter(status='recovered')
    rLen = len(r)
    context = {'Posts': Post.objects.all(),'infected': iLen, 'uninfected': uLen, 'recovered': rLen}
    return render(request, 'loginApp/home.html',context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
            return redirect('login')
        else:
            if request.POST.get('address') == '':
                errmsg = "must enter an address"
            else:
                errmsg = ''
    else:
        form = UserRegisterForm()
        
    return render(request, 'loginApp/register.html', {'form': form, 'err' : errmsg})
