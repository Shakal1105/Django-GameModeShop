# Generated by Django 3.2.3 on 2021-05-26 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_rename_notebook_games'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]