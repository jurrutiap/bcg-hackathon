from email.message import Message
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django import forms
from django.core.files.storage import FileSystemStorage

import os
import sys
sys.path.append("..")

import utils.shift_system as shift

def home(request):
    return render(request, 'index.html')

def shift_view(request, *textC):
    if request.method == "POST":
        if 'encrypt' in request.POST:
            message = request.POST['textC']
            # data = shift.encrypt(message, k)
            data = 'hola'
            return render(request, 'shift_system.html', {'data':data, 'clear': message, 'mapbox_access_token': 'pk.eyJ1IjoianVycnV0aWFwIiwiYSI6ImNsbmY0YmdjOTBoNGwya3JpbnB3dDN4b3UifQ.U7ld5qVva8zy9ZibouV10g' })

        if 'desencrypt' in request.POST:
            message = request.POST['textE']
            k= shift.k(request.POST['k2'])
            data = shift.desencrypt(message, k)
            return render(request, 'shift_system.html', {'data':data, 'cipher': message, 'k2':k})

    return render(request, 'shift_system.html')
