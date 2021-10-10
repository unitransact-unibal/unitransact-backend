from django_seed import Seed
from django.contrib.auth import get_user_model

from .models import DonationsWalletTransaction


class DonationsWalletTransactionSeeder:
    def gen_user(self, seeder, user_ids):
        # print(user_ids)
        user_id = seeder.faker.random_elements(user_ids, length=1, unique=True)

        user_id = user_id[0]
        user = get_user_model().objects.get(id=user_id)

        return user

    def seed(self, count):
        seeder = Seed.seeder()

        users = get_user_model().objects.values_list('id', flat=True)
        users = list(users)

        seeder.add_entity(DonationsWalletTransaction, count, {
            'user_id': lambda x: self.gen_user(seeder, users),
            'amount': lambda x: seeder.faker.random_int(min=500, max=1_000_000, step=10),
            'transaction_type': lambda x: seeder.faker.random_element(elements=('db', 'cr'))
        })

        inserted_pks = seeder.execute()
        return inserted_pks
