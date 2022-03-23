from django.shortcuts import render
from django.db import models
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UploadImageForm, Animal
from . import forms
from .models import Animal

def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        filename = request.POST['title']
        if form.is_valid():
            upload(request.FILES['files'], filename)
            return HttpResponse("<h2>Image uploaded successful!</h2>")
        else:
            return HttpResponse("<h2>Image uploaded not successful!</h2>")
    form = UploadImageForm()
    return render(request, 'lession04/upload.html', {'form': form})

def upload(f, filename):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)

def addAnimal(request):
    context = {}

    form = Animal(request.POST or None, request.FILES or None)

    if form.is_valid():
        # save the form data to model
        form.save()
        alert = 'Update Successfully. Thank you!'
        return HttpResponseRedirect( "/lession04/index_animal/")
    else:
        alert = 'Data is invalid, try again!'
    context['form'] = form
    return render(request, "lession04/add_animal.html", context)

def indexAnimal(request):
    listAnimal = Animal.objects.order_by('id')[:1000]
    context = {'listAnimal': listAnimal}
    return render(request, 'lession04/index_animal.html', context)
