from django.core.management.base import BaseCommand
from students.seeder import seed as seed_students
from parents.seeder import seed as seed_parents
from users.seeder import seed as seed_users


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        inserted = seed_users(100)
        print(inserted)

        inserted = seed_students(30)
        print(inserted)

        inserted = seed_parents(30)
        print(inserted)
