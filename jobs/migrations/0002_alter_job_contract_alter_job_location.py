# Generated by Django 4.1.7 on 2023-03-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='contract',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Hourly', 'Hourly')], max_length=150),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Bangalore', 'Bangalore'), ('Pune', 'Pune')], max_length=50),
        ),
    ]
