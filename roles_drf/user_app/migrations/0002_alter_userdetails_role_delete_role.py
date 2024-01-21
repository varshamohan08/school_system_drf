# Generated by Django 5.0.1 on 2024-01-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Staff', 'Staff'), ('Admin', 'Admin'), ('Editor', 'Editor')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
