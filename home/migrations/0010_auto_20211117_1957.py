# Generated by Django 3.2.5 on 2021-11-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_ds_question_ds_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DS_Questions',
            new_name='Dbms',
        ),
        migrations.RenameModel(
            old_name='DBMS_Questions',
            new_name='Ds',
        ),
    ]
