from django_seed import Seed
from .models import Student
from django.contrib.auth import get_user_model


def gen_user_id(seeder, user_ids):
    user_id = seeder.faker.random_elements(user_ids, length=1, unique=True)

    user_id = user_id[0]
    user = get_user_model().objects.get(id=user_id)

    return user


def seed(count):
    seeder = Seed.seeder()

    users = get_user_model().objects.values_list('id', flat=True)
    users = list(users)

    seeder.add_entity(Student, count, {
        "admission_number": lambda x: seeder.faker.random_int(min=1000, max=9999),
        "telephone": lambda x: seeder.faker.phone_number(),
        'user_id': lambda x: gen_user_id(seeder, users)
    })

    inserted_pks = seeder.execute()
    return inserted_pks
