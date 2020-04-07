from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
# Create your views here.


class LandingClass(View):
    templates = 'Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.templates,{})
