# Generated by Django 4.2.5 on 2024-02-05 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='matric_number',
            new_name='matric',
        ),
    ]
