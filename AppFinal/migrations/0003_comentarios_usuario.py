# Generated by Django 4.1.2 on 2022-12-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0002_remove_blogs_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.CharField(default='', max_length=50),
        ),
    ]