from django.core.management.base import BaseCommand
from students.seeder import seed_students
from students.seeder import StudentParentSeeder, StudentWalletTransactionSeeder
from parents.seeder import seed as seed_parents
from users.seeder import seed as seed_users
from schools.seeder import seed as seed_schools


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        inserted = seed_users(200)
        print(inserted)

        inserted = seed_schools(30)
        print(inserted)

        inserted = seed_students(30)
        print(inserted)

        inserted = seed_parents(30)
        print(inserted)

        sd = StudentParentSeeder()
        inserted = sd.seed(30)
        print(inserted)

        sd = StudentWalletTransactionSeeder()
        inserted = sd.seed(30)
        print(inserted)
