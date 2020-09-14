from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages


def contact(request):
    contact_form = ContactForm
    if request.method == 'POST':
        form = contact_form(data=request.POST)

        if form.is_valid():
            contact_email = request.POST.get(' contact_email')

            template = get_template('contact/contact_form.txt')
            content = {
                'contact_name': request.POST.get('contact_name'),
                'contact_email': request.POST.get('contact_email'),
                'contact_number': request.POST.get('contact_number'),
                'message': request.POST.get('message'),
                'class_type': request.POST.get('class_type'),
                'language_level': request.POST.get('language_level')
            }

            content = template.render(content)
            email = EmailMessage(
                'Nova prijava za časove ',
                content,
                'Charla Con Ivona' + '',
                ['ognjenovicivona@gmail.com'],
                reply_to=[contact_email]
            )

            email.send()

        messages.info(request, 'Prijava je uspešno poslata')
        return redirect('contact')

    return render(request, 'contact/contact.html', {'contact_form': contact_form})
"""ognjenovicivona@gmail.com"""

