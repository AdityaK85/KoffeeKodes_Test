# Generated by Django 5.0.2 on 2024-05-20 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0004_alter_interviewmaster_options_alter_myuser_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='phone_no',
            new_name='role',
        ),
    ]
