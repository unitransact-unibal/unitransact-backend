from django_seed import Seed

from parents.models import Parent
from schools.models import School
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

    schools = School.objects.values_list('user_id', flat=True)
    schools = list(schools)

    to_remove = schools
    for item in to_remove:
        i = users.index(item)
        users.pop(i)

    seeder.add_entity(Student, count, {
        "admission_number": lambda x: seeder.faker.random_int(min=1000, max=9999),
        "telephone": lambda x: seeder.faker.phone_number(),
        'user_id': lambda x: gen_user_id(seeder, users)
    })

    inserted_pks = seeder.execute()
    return inserted_pks


def seed_student_parents(count):
    seeder = Seed.seeder()

    students = Student.objects.values_list('id', flat=True)
    students = list(students)

    parents = Parent.objects.values_list('id', flat=True)
    parents = list(parents)

    students_parents = []
    for student in students:
        for parent in parents:
            students_parents.append('{}-{}'.format(student, parent))

    student_parent = seeder.faker.random_elements(
        students_parents, length=1, unique=True
    )
    student_parent = student_parent[0].split('-')
    student = Student.objects.get(id=student_parent[0])
    parent = Parent.objects.get(id=student_parent[1])

    seeder.add_entity(Parent, count, {
        'student_id': lambda x: gen_user_id(seeder, student),
        'parent_id': lambda x: gen_user_id(seeder, parent),
    })
