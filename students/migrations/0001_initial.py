# Generated by Django 3.2.7 on 2021-10-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('telephone', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('school_id', models.PositiveIntegerField()),
            ],
        ),
    ]
