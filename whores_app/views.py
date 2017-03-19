from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

def index(request):
    user = request.user
    #if not user.is_authenticated():
    #     return HttpResponseRedirect("login")

    is_whore = user.groups.filter(name__in=['whore']).exists()
    print (is_whore)
    return render(request, 'whores_app/index.html',{'user': user, 'is_whore': is_whore})

def about(request):
    context = "x"
    return render(request, 'whores_app/index.html', context)
