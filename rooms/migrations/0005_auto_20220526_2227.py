# Generated by Django 2.2.5 on 2022-05-26 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20220525_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='amanities',
            new_name='amenities',
        ),
    ]