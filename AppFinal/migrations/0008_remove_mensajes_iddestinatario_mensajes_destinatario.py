# Generated by Django 4.1.2 on 2022-12-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0007_alter_comentarios_idblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='iddestinatario',
        ),
        migrations.AddField(
            model_name='mensajes',
            name='destinatario',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
