from django_seed import Seed
from .models import Student


def seed():
    seeder = Seed.seeder()
    seeder.add_entity(Student, 15, {
        "admission_number": seeder.faker.random_digit_not_null(),
        "address": lambda: seeder.faker.address(),
    })

    inserted_pks = seeder.execute()
    return inserted_pks
