from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)

class Questions(models.Model):
    question = models.CharField(max_length=200, primary_key=True)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    answer = models.PositiveIntegerField()

class Scores(models.Model):
    score = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
