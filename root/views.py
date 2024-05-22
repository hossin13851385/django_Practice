from django.shortcuts import render
from .models import *

def home(request):
    context = {
        'service' : Service.objects.all(),
        'team' : team.objects.all(),
        'skill' : skill.objects.all(),
        'pro' : portfolio.objects.all()
    }
    return render(request ,'root/index.html' , context=context)