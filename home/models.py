from django.db import models

# Create your models here.
class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'

    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    # done = models.BooleanField(null=False, blank=False, default=False)
    def __str__(self):
        return self.email
