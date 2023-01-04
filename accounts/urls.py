from django.urls import path
from django.urls import reverse_lazy
from . import views
urlpatterns = [
    path('',views.diendan,name = "diendan"),
    path('login',views.login,name = "login"),
    #path('login/',views.login,name = "login2"), 
    #path('login/',views.login,name = "login2"), 
]