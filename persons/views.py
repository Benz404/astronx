from email.message import Message
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from main.models import audit_wealth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('superpage')
        else:
            messages.success(request,("wrong username or password !!! please try again"))
            return redirect('login')
    return render(request,'login.html')
    
@login_required
def superpage(request,*args, **kwargs):
    stored_data=audit_wealth.objects.all().order_by('-created')
    dna_data={
        'dataline':stored_data,
    }
    return render(request,'superpage.html',dna_data)

def logout_user(request):
    logout(request)
    messages.success(request,("you are logged out !!!"))
    return redirect('/')

@login_required
def delete(request,pk):
  data = get_object_or_404(audit_wealth, pk=pk)
  data.delete()
  messages.success(request,("The data is deleted successfully"))
  return redirect('superpage')

@login_required
def edit(request,pk):
    stored_data = get_object_or_404(audit_wealth, pk=pk)
    dna_data={
        'dataline':stored_data,
    }
    return render(request,'editpage.html',dna_data)
