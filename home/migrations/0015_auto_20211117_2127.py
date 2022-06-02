# Generated by Django 3.2.5 on 2021-11-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_question1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionsdbms',
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
        migrations.CreateModel(
            name='Questionsds',
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
            name='Question1',
        ),
    ]