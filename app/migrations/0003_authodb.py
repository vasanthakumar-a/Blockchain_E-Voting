# Generated by Django 3.2.7 on 2021-09-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_address_addressdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='authoDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.IntegerField()),
            ],
        ),
    ]