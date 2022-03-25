from email import message
from itertools import product
from unittest import result
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def sendMail(request):

    messageSent = False

    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = "Send email from Django"
            message = cd['message']
            recipient = cd['recipient']

            if send_mail(subject, message,
                        settings.DEFAULT_FROM_EMAIL, [recipient]):

                messageSent = True
            
    else:
        form = EmailForm()
    return render(request, 'lession05/send-mail.html',{
        'form':form,
        'messageSent':messageSent
    })
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TLL',DEFAULT_TIMEOUT )
@api_view(['GET'])
def get_products_cached(request):
    if 'products' in cache:
        #get result from cache
        products= cache.get('products')
        return Response(result, status = status.HTTP_201_CREATED)
    else:
        products =Product.objects.all()
        results = [product.to_json for product in products]
       # store data in cache
        cache.set('products', results, timeout=CACHE_TTL)
        return Response(result, status = status.HTTP_201_CREATED)
