from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout 
from django.shortcuts import redirect

# Create your views here.


class DashboardClass(LoginRequiredMixin,View):
    templates_okidoki = 'Dashboard/Dashboard.html'
    def get (self,request,*args,**kwargs):
        #printn("GET DE DASHBOARD")
        return render(request,self.templates_okidoki,{})
