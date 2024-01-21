# Generated by Django 5.0.1 on 2024-01-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Created', 'Created'), ('Approved', 'Approved')], max_length=20, null=True)),
            ],
        ),
    ]