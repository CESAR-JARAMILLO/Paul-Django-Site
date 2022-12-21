from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

def index(request):
    return render(request, 'base/index.html')

def thankyou(request):
    return render(request, 'base/thankyou.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('base/emails/contactform.html', {
                'name':name,
                'email':email,
                'content':content
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@code.com', ['cesarjaramillodev@gmail.com'], html_message=html)

            return redirect('/thankyou/')
    else:
        print('error')
        form = ContactForm()
    
    return render(request, 'base/contact.html', {'form':form})