# Generated by Django 4.1.2 on 2022-12-16 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='email',
        ),
    ]