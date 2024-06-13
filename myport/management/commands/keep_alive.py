# myapp/management/commands/keep_alive.py
import time
from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Keeps the Django application alive by making periodic requests'

    def handle(self, *args, **kwargs):
        while True:
            try:
                # Replace 'http://yourdomain.com/' with the URL of your application
                response = requests.get('https://nazrulhudashanto.onrender.com/')
                if response.status_code == 200:
                    self.stdout.write(self.style.SUCCESS('Successfully kept application alive.'))
                else:
                    self.stdout.write(self.style.ERROR('Failed to keep application alive.'))
            except requests.RequestException as e:
                self.stdout.write(self.style.ERROR(f'Error keeping application alive: {str(e)}'))

            # Sleep for 14 minutes and 59 seconds
            time.sleep(14 * 60 + 59)
