from django.shortcuts import render
from auth_app.forms import userform,userinfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from auth_app.models import Userinfo



# Create your views here.
def login_page(request):
    dict={}
    return render(request,'login_app/login.html',context=dict)

def index(request):
    dict={}
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_basic_info=User.objects.get(pk=user_id)
        user_more_info=Userinfo.objects.get(user__pk=user_id)
        dict={'user_basic_info':user_basic_info,'user_more_info':user_more_info}
    return render(request,'login_app/index.html',context=dict)


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('login_app:index'))

            else:
                return HttpResponse('Account is not Active!!')
        else:
            return HttpResponse("LOg In are Wrong")
    else:
        #return render(request,'login_app/login.html',context={})
        return HttpResponseRedirect(reverse('login_app:login_page'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:index'))

def register(request):

    registered=False

    if request.method=='POST':
        user_form=userform(data=request.POST)
        user_info=userinfo(data=request.POST)

        if user_form.is_valid() and user_info.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            user_info=user_info.save(commit=False)
            user_info.user=user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic=request.FILES['profile_pic']

            user_info.save()
            registered=True

    else:
        user_form=userform()
        user_info=userinfo()

#

    dic={'user_form':user_form,'user_info':user_info,'registered':registered}
    return render(request,'login_app/register.html',context=dic)
