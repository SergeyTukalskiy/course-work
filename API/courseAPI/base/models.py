from django.db import models


# Create your models here.


class Item(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Student(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    username = models.CharField()
    password = models.CharField()
    title = models.CharField
    teacherName = models.CharField
    teacherId = models.IntegerField
    steps = models.CharField()
