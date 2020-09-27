from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


def contact(request):
    """
    Renders contact template and contact 
    form.
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            create_contact_form = Contact(
                name=request.POST.get('name'),
                comment=request.POST.get('comment'),
                email=request.POST.get('email'),
                user_id=request.user
            )
            create_contact_form.save()
        else:
            create_contact_form = Contact(
                name=request.POST.get('name'),
                comment=request.POST.get('comment'),
                email=request.POST.get('email'),
            )
            create_contact_form.save()

        # Send Email
        send_mail(
            'New Form Submission',
            'Hi Admin,\n\nYou have a new contact message. Sign '
            'into the admin panel to view.\n\nRegards,'
            'n\nHello World Apparel',
            'helloworldapparel@gmail.com',
            [EMAIL_HOST_USER],
            fail_silently=True
        )

        messages.success(request, 'Contact form successfully submitted. We will be in touch!')
        return redirect(reverse('contact_success'))

    context = {
        'form': ContactForm
    }
    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return render(request, "contact/contact_success.html")