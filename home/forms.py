from django.forms import ModelForm
from .models import ContactUs


class ContactForm(ModelForm):
    # required_css_class = 'required-field'
    # error_css_class = 'error-field'
    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]