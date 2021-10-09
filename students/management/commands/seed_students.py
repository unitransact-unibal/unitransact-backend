from django.core.management.base import BaseCommand
from students.seeder import seed


class Command(BaseCommand):
    help = 'seed students table'

    def handle(self, *args, **options):
        inserted = seed()
        print(inserted)
