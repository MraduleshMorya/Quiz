# Generated by Django 3.2.5 on 2022-05-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20220526_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='c_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='dbms_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ds_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='percentage',
            field=models.IntegerField(blank=True, default=0, null='True'),
        ),
    ]
