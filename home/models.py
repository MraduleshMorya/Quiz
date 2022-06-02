from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=20, null=True,blank=True)
    lastname = models.EmailField(max_length=30, null=True,blank=True)
    c_score = models.IntegerField(null=True,blank=True,default=0)
    ds_score = models.IntegerField(null=True,blank=True,default=0)
    dbms_score = models.IntegerField(null=True,blank=True,default=0)
    percentage = models.IntegerField(null='True',blank=True,default=0)

    def __str__(self):
        return self.name


class Questions(models.Model):
    Question = models.CharField(max_length=400, null=True,blank=True)
    Option1 = models.CharField(max_length=300, null=True,blank=True)
    Option2 = models.CharField(max_length=300, null=True,blank=True)
    Option3 = models.CharField(max_length=300, null=True,blank=True)
    Option4 = models.CharField(max_length=300, null=True,blank=True)
    Answer = models.CharField(max_length=300, null=True,blank=True)

    def __str__(self):
        return self.Question


class Questionsds(models.Model):
    Question = models.CharField(max_length=400, null=True)
    Option1 = models.CharField(max_length=300, null=True)
    Option2 = models.CharField(max_length=300, null=True)
    Option3 = models.CharField(max_length=300, null=True)
    Option4 = models.CharField(max_length=300, null=True)
    Answer = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.Question


class Questionsdbms(models.Model):
    Question = models.CharField(max_length=400, null=True)
    Option1 = models.CharField(max_length=300, null=True)
    Option2 = models.CharField(max_length=300, null=True)
    Option3 = models.CharField(max_length=300, null=True)
    Option4 = models.CharField(max_length=300, null=True)
    Answer = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.Question
