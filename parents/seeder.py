from django_seed import Seed

from schools.models import School
from students.models import Student
from .models import Parent
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

    # remove ids of students and schools
    students = Student.objects.values_list('user_id', flat=True)
    students = list(students)

    schools = School.objects.values_list('user_id', flat=True)
    schools = list(schools)

    to_remove = students + schools
    for item in to_remove:
        i = users.index(item)
        users.pop(i)

    seeder.add_entity(Parent, count, {
        "national_id": lambda x: seeder.faker.random_int(min=100_000, max=999_999, unique=True),
        "telephone": lambda x: seeder.faker.phone_number(),
        "country": lambda x: seeder.faker.country_code(),
        'user_id': lambda x: gen_user_id(seeder, users)
    })

    inserted_pks = seeder.execute()
    return inserted_pks
