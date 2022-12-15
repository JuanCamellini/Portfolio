from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "web/index.html")

def thanks(request):
    return render(request, "web/thanks.html")