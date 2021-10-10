from django.core.management.base import BaseCommand
from students.seeder import seed as seed_students
from parents.seeder import seed as seed_parents


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        inserted = seed_students(3)
        print(inserted)

        inserted = seed_parents(30)
        print(inserted)
