from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Person

def index(request):
    all_people = Person.objects.order_by('id')[:10]
    context = {'all_people': all_people}
    return render(request, 'lession02/index.html', context)

# def detail(request, person_id):
#     try:
#         person = Person.objects.get(pk=person_id)
#     except Person.DoesNotExist:
#         raise Http404("Person does not exist")
#     return render(request, 'assign_02_app/detail.html', {'person': person})