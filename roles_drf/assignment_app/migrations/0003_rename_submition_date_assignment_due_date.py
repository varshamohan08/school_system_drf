# Generated by Django 5.0.1 on 2024-01-20 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0002_assignment_submition_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='submition_date',
            new_name='due_date',
        ),
    ]
