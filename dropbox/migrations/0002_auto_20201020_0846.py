# Generated by Django 3.0.5 on 2020-10-20 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dropbox', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dropbox',
            old_name='name',
            new_name='fileName',
        ),
    ]
