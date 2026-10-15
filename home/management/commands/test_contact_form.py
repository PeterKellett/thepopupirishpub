from django.core.management.base import BaseCommand
from home.views import mailNewContact
from datetime import datetime

class Command(BaseCommand):
    help = 'Triggers an automated monthly test submission for the Contact Us form'

    def handle(self, *args, **kwargs):
        # The script checks the calendar day
        today = datetime.now()
        if today.day != 15:
            self.stdout.write(self.style.SUCCESS('Skipping: Today is not the first day of the month.'))
            return

        self.stdout.write('Initiating automated contact form test...')

        # Mock data block matching your website payload structure
        test_data = {
            'name': 'Automated Monthly Test Bot',
            'email': 'thepopupirishpub@gmail.com',
            'message': f'This is an automated system health check sent on {today.strftime("%b %d, %Y")}.'
        }

        try:
            # Executes your exact Google SMTP SSL mail engine
            mailNewContact(test_data)
            self.stdout.write(self.style.SUCCESS('Success: Automated test email sent successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failure: Test script failed with error: {str(e)}'))
