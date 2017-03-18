from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

def index(request):
    context = "12"
    current_user = request.user
    print (current_user)
    return render(request, 'whores_app/index.html',{'context': context, 'current_user': current_user})

def about(request):
    context = "x"
    return render(request, 'whores_app/index.html', context)
