# Generated by Django 4.0.4 on 2022-05-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_user_project_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='users',
            new_name='user',
        ),
    ]
