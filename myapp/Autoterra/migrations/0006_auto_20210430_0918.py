# Generated by Django 3.2 on 2021-04-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autoterra', '0005_auto_20210430_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blibliotheque',
            options={'ordering': ['Animal', 'Image', 'Humidite']},
        ),
        migrations.AddField(
            model_name='blibliotheque',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
