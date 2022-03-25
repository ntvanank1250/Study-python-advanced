from email import message
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