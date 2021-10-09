from django_seed import Seed
from .models import Student


def seed(count):
    seeder = Seed.seeder()
    seeder.add_entity(Student, count, {
        "admission_number": lambda x: seeder.faker.random_digit_not_null(),
        "telephone": lambda x: seeder.faker.phone_number(),
    })

    inserted_pks = seeder.execute()
    return inserted_pks