# Generated by Django 4.1.5 on 2023-04-26 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_home_resume_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='resume',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='resume_title',
            new_name='title',
        ),
    ]