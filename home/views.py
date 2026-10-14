from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
import json
from . models import ContactUs
import os
# Create your views here.
def index(request):
    """ A view to return the index page """
    print("request = ", request)
    
    if request.method == "POST":
        # 1. Parse your incoming data streams safely
        if request.content_type == 'application/json':
            try:
                data = json.load(request)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON structure'}, status=400)
        else:
            data = {
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "message": request.POST.get("message")
            }
            
        print("Processed Form Data = ", data)
        
        # 2. INDENTED: This validation block must only ever execute on a POST request!
        if data.get("name") and data.get("email"):
            newContact = ContactUs(
                name=data["name"],
                email=data["email"],
                message=data["message"]
            )
            newContact.save()
            mailNewContact(data)
            
            # Return appropriate response depending on input format
            if request.content_type == 'application/json':
                return JsonResponse({'status': 'Checkout Complete'}, status=200)
            return redirect('/en/#contact')
            
    # 3. Clean page requests (GET) skip the blocks above entirely and load the page normally
    context = {}
    return render(request, 'home/index.html', context)

def mailNewContact(data):
    print("mailNewContact = ", data)
    name = data.get("name", "No Name Given")
    email = data.get("email", "No Email Given")
    message = data.get("message", "No Message Body")

    # Clean, single-string formatting with explicit newlines (\n)
    notify_message = (
        f"Received message below from:\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"----------------------------------------\n\n"
        f"{message}"
    )
    print("Sending email from:", settings.DEFAULT_FROM_EMAIL)
    print("Sending email to:", settings.NOTIFY_EMAIL)

    send_mail(
        subject="Website Contact Us form submission",
        message=notify_message,
        from_email=settings.DEFAULT_FROM_EMAIL, # Must be your exact Gmail address string!
        recipient_list=[settings.NOTIFY_EMAIL],  # info@thepopupirishpub.com
        fail_silently=False, # Force Django to throw an explicit error in logs if it fails!
    )


def aboutus(request):
    return render(request, 'home/aboutus.html')

def kiwobar(request):
    return render(request, 'home/kiwobar.html')

def guinnessbar(request):
    return render(request, 'home/guinnessbar.html')

def mobilebar(request):
    return render(request, 'home/mobilebar.html')

def custombar(request):
    return render(request, 'home/custombar.html')


# class SuccessView(TemplateView):
#     template_name = "success.html"


# class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)