from django.shortcuts import render, redirect
from forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
#  https://hellowebapp.com/news/tutorial-setting-up-a-contact-form-with-django/


def contact(request):
    """Contact."""
    form_class = ContactForm

    if request.method == 'POST':
            form = form_class(data=request.POST)

            if form.is_valid():
                contact_name = request.POST.get(
                    'contact_name', '')
                contact_email = request.POST.get(
                    'contact_email', '')
                form_content = request.POST.get('content', '')

                # Email the profile with the contact information
                template = get_template('contact/contact_template.txt')
                content = template.render({
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content
                })

                email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + '',
                    ['example@example.com'],
                    headers={'Reply-To': contact_email}
                )
                email.send()
                return render(request, 'contact/template.html', {
                    'send': True
                })

    return render(request, 'contact/template.html', {
        'form': form_class,
    })
