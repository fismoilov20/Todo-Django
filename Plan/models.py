from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    course = models.PositiveSmallIntegerField()
    std_id = models.PositiveIntegerField(unique=True)
    def __str__(self) -> str:
        return self.name

class Plan(models.Model):
    heading = models.CharField(max_length=150)
    date = models.DateTimeField(null=True, blank=True)
    details = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.heading}, {self.student.name}"

class Account(models.Model):
    fullname=models.CharField(max_length=50)
    group = models.CharField(max_length=50, blank=True)
    student_id = models.CharField(max_length=50, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)                   # OneToOne
    def __str__(self) -> str:
        return self.fullname

class Todo(models.Model):
    heading = models.CharField(max_length=150)
    date = models.DateTimeField(null=True, blank=True)
    details = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    student = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)   # OneToOne
    def __str__(self) -> str:
        return f"{self.heading}"
