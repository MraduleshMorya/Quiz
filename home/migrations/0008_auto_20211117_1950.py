# Generated by Django 3.2.5 on 2021-11-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211117_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='DS_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=200, null=True)),
                ('Option1', models.CharField(max_length=200, null=True)),
                ('Option2', models.CharField(max_length=200, null=True)),
                ('Option3', models.CharField(max_length=200, null=True)),
                ('Option4', models.CharField(max_length=200, null=True)),
                ('Answer', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DS_Questions',
        ),
    ]