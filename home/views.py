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
    # DEVELOPMENT = os.getenv('DEVELOPMENT')
    # print("DEVELOPMENT = ", DEVELOPMENT)
    print("request = ", request)
    if request.method == "POST":
        # 1. Handle JavaScript Fetch/JSON data
        if request.content_type == 'application/json':
            data = json.load(request)
        else:
            # 2. Handle standard HTML Form data fallback
            data = {
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "message": request.POST.get("message")
            }
            
        print("Processed Form Data = ", data)
        # Guard clause: ensure data isn't empty before saving
        if data["name"] and data["email"]:
            newContact = ContactUs(
                name=data["name"],
                email=data["email"],
                message=data["message"]
            )
            newContact.save()
            mailNewContact(data)

            # Return JSON if it was an AJAX request, otherwise redirect normally
            if request.content_type == 'application/json':
                return JsonResponse({'status': 'Checkout Complete'}, status=200)
            return redirect('home') # Or wherever your landing route name points
            
    context = {}
    return render(request, 'home/index.html', context)


def mailNewContact(data):
    print("mailNewContact = ", data)
    name = data["name"]
    email = data["email"]
    message = data["message"]

    notify_message = f"""
        Received message below from 
        {name},
        {email}
        ________________________

        {message}
        """
    send_mail(
        subject="Website Contact Us form submission",
        message=notify_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.NOTIFY_EMAIL],
    )

    # acknowledgement_message = f"""
    #     Thank you for your query.
    #     we will be in contack with you soon.
    #     Kind regards
    #     The Pop Up Irish Pub
    #     """
    # send_mail(
    #     subject="Thank you for your query",
    #     message=acknowledgement_message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[{email}]
    # )




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