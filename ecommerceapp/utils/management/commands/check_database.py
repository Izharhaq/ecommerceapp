from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Check the configured database'

    def handle(self, *args, **kwargs):
        databases = settings.DATABASES
        for alias, config in databases.items():
            self.stdout.write(f"Database alias: {alias}")
            for key, value in config.items():
                self.stdout.write(f"  {key}: {value}")
