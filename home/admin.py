from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'name',
        'email',
        'message',
    )
# Register your models here.
admin.site.register(ContactUs, ContactUsAdmin)

