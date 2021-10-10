from django_seed import Seed
from .models import Parent


def seed(count):
    seeder = Seed.seeder()
    seeder.add_entity(Parent, count, {
        "national_id": lambda x: seeder.faker.random_int(min=100_000, max=999_999),
        "telephone": lambda x: seeder.faker.phone_number(),
    })

    inserted_pks = seeder.execute()
    return inserted_pks
