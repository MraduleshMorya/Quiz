# Generated by Django 3.2.5 on 2021-11-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]