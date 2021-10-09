from django_seed import Seed
from .models import Student


def seed():
    seeder = Seed.seeder()
    seeder.add_entity(Student, 15)

    inserted_pks = seeder.execute()
    return inserted_pks
