from django_seed import Seed
from django.contrib.auth import get_user_model

from parents.models import Parent
from schools.models import School
from .models import Student, StudentParent, StudentWalletTransaction


def gen_user_id(seeder, user_ids):
    # print(user_ids)
    user_id = seeder.faker.random_elements(user_ids, length=1, unique=True)

    user_id = user_id[0]
    user = get_user_model().objects.get(id=user_id)

    return user

def gen_school_id(seeder, school_ids):
    school_id = seeder.faker.random_elements(school_ids, length=1, unique=True)

    school_id = school_id[0]
    school = School.objects.get(id=school_id)

    return school

def seed_students(count):
    seeder = Seed.seeder()

    users = get_user_model().objects.values_list('id', flat=True)
    users = list(users)

    schools = School.objects.values_list('user_id', flat=True)
    schools = list(schools)

    to_remove = schools
    for item in to_remove:
        i = users.index(item)
        users.pop(i)

    schools = School.objects.values_list('id', flat=True)
    schools = list(schools)

    seeder.add_entity(Student, count, {
        "admission_number": lambda x: seeder.faker.random_int(min=1000, max=9999),
        "telephone": lambda x: seeder.faker.phone_number(),
        "country": lambda x: seeder.faker.country_code(),
        "school_id": lambda x: gen_school_id(seeder, schools),
        'user_id': lambda x: gen_user_id(seeder, users)
    })

    inserted_pks = seeder.execute()
    return inserted_pks


class StudentParentSeeder():
    def __init__(self):
        self.students_parents = []
        self.student_parent = -1

    def gen_student(self):
        student = Student.objects.get(id=self.student_parent[0])
        return student

    def gen_parent(self, seeder):
        self.student_parent = seeder.faker.random_elements(
            self.students_parents, length=1, unique=True
        )
        self.student_parent = self.student_parent[0].split('-')
        parent = Parent.objects.get(id=self.student_parent[1])
        return parent

    def seed(self, count):
        seeder = Seed.seeder()

        students = Student.objects.values_list('id', flat=True)
        students = list(students)

        parents = Parent.objects.values_list('id', flat=True)
        parents = list(parents)

        for student in students:
            for parent in parents:
                self.students_parents.append('{}-{}'.format(student, parent))

        student_parent = seeder.faker.random_elements(
            self.students_parents, length=1, unique=True
        )
        student_parent = student_parent[0].split('-')
        student = Student.objects.get(id=student_parent[0])
        parent = Parent.objects.get(id=student_parent[1])

        # django-seed sorts the fields in alphabetical order then seeds so...
        seeder.add_entity(StudentParent, count, {
            # Get a unique student_parent combination, and populate the parent
            'parent_id': lambda x: self.gen_parent(seeder),
            # Use the previously selected student_parent combination here too
            'student_id': lambda x: self.gen_student(),
        })

        inserted_pks = seeder.execute()
        return inserted_pks


class StudentWalletTransactionSeeder:
    def gen_user(self, seeder, user_ids):
        # print(user_ids)
        user_id = seeder.faker.random_elements(user_ids, length=1, unique=True)

        user_id = user_id[0]
        user = get_user_model().objects.get(id=user_id)

        return user

    def gen_student(self, seeder, student_ids):
        student_id = seeder.faker.random_elements(
            student_ids, length=1, unique=True)

        student_id = student_id[0]
        student = Student.objects.get(id=student_id)

        return student

    def seed(self, count):
        seeder = Seed.seeder()

        users = get_user_model().objects.values_list('id', flat=True)
        users = list(users)

        students = Student.objects.values_list('id', flat=True)
        students = list(students)

        seeder.add_entity(StudentWalletTransaction, count, {
            'user_id': lambda x: self.gen_user(seeder, users),
            'student_id': lambda x: self.gen_student(seeder, students),
            'amount': lambda x: seeder.faker.random_int(min=500, max=5000, step=10),
            'transaction_type': lambda x: seeder.faker.random_element(elements=('db', 'cr'))
        })

        inserted_pks = seeder.execute()
        return inserted_pks
