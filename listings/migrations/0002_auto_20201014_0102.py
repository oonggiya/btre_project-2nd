# Generated by Django 3.1.2 on 2020-10-14 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_publised',
            new_name='is_published',
        ),
    ]
