from django.core.management.base import BaseCommand
from students.seeder import seed as seed_students


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        inserted = seed_students(30)
        print(inserted)
