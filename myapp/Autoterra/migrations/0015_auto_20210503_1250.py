# Generated by Django 3.2 on 2021-05-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Autoterra', '0014_bibliotheque'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question_niv',
        ),
    ]