from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

def index(request):
    return render(request, 'base/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']

            html = render_to_string('base/emails/contactform.html', {
                'name':name,
                'email':email,
                'subject':subject
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@code.com', ['cesarjaramillodev@gmail.com'], html_message=html)

            return redirect('/')
    else:
        form = ContactForm()
    
    return render(request, 'base/contact.html', {'form':form})