# Generated by Django 4.1 on 2022-08-14 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_rename_coursemodel_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='picture',
            new_name='image',
        ),
    ]
