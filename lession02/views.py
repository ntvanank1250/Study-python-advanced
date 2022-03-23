from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Person
from .form import PersonForm

def index(request):
    all_people = Person.objects.order_by('id')[:1000]
    context = {'all_people': all_people}
    return render(request, 'lession02/index.html', context)

def detail(request, person_id):
    try:
        infoPerson = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'lession02/detail.html', {'infoPerson': infoPerson})

def formInput(request):
    context = {}

    form = PersonForm(request.POST or None, request.FILES or None)

  
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/lession02/thankyou/')

    context['form'] = form
    return render(request, "lession02/formInput.html", context)

def thankYou(request):
    return render(request,"lession02/thankyou.html")