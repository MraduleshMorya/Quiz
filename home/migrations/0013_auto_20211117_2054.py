# Generated by Django 3.2.5 on 2021-11-17 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_questions1_questions2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Questions1',
        ),
        migrations.DeleteModel(
            name='Questions2',
        ),
    ]
