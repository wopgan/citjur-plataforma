# Generated by Django 4.1.7 on 2023-03-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productscitjur', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buycoincj',
            name='qnt',
        ),
    ]