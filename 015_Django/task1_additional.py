from decimal import Decimal

from django.db import models
from datetime import timedelta
# Create your models here.
class Curators(models.Model):
    name = models.CharField(max_length=100,null=False)
    surname = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
class Faculties(models.Model):
    name = models.CharField(null=False, max_length=100)
    def __str__(self):
        return self.name
class Departments(models.Model):
    name = models.CharField(null=False,max_length=100)
    First = 'Fi'
    Second = 'Se'
    Third = 'Th'
    Fourth = 'Fo'
    Fiveth = 'Fv'
    day_CHOICES = [
        (First, '1'),
        (Second, '2'),
        (Third, '3'),
        (Fourth, '4'),
        (Fiveth, '5')
    ]
    building = models.CharField(max_length=2, choices=day_CHOICES, default=First)
    financing = models.DecimalField(decimal_places=2, max_digits=10, default=1)
    facultyId=models.ForeignKey(Faculties, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Groups(models.Model):
    name = models.CharField(null=False, max_length=100)
    First = 'Fi'
    Second = 'Se'
    Third = 'Th'
    Fourth = 'Fo'
    Fiveth = 'Fv'
    day_CHOICES = [
        (First, '1'),
        (Second, '2'),
        (Third, '3'),
        (Fourth, '4'),
        (Fiveth, '5')
    ]
    year = models.CharField(max_length=2, choices=day_CHOICES, default=First)
    departamentid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
class GroupsCurators(models.Model):

    curatorId=models.ForeignKey(Curators,on_delete=models.CASCADE,null=True)
    groupId=models.ForeignKey(Groups,on_delete=models.CASCADE,null=True)
class Students(models.Model):
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    Zero='Ze'
    First = 'Fi'
    Second = 'Se'
    Third = 'Th'
    Fourth = 'Fo'
    Fiveth = 'Fv'
    day_CHOICES = [
        (Zero,'0'),
        (First, '1'),
        (Second, '2'),
        (Third, '3'),
        (Fourth, '4'),
        (Fiveth, '5')
    ]
    rating = models.CharField(max_length=2, choices=day_CHOICES, default=Zero)
    def __str__(self):
        return self.name
class Subjects(models.Model):
    name = models.CharField(null=False, max_length=100,blank=False,unique=True)
    def __str__(self):
        return self.name
class Teachers(models.Model):
    name = models.CharField(null=False, max_length=100, blank=False, unique=True)
    surname = models.CharField(null=False, max_length=100, blank=False, unique=True)
    IsProfessor=models.BooleanField(default=False)
    salary = models.DecimalField(decimal_places=2, max_digits=10, default=1)
    def __str__(self):
        return self.name
class GroupsStudents(models.Model):
    groupId = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)
    studentId = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
class Lectures(models.Model):
    date=models.DateField(null=False)
    subjectId=models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)
    teacherId=models.ForeignKey(Teachers,on_delete=models.CASCADE,null=True)
class GroupsLectures(models.Model):
    curatorId = models.ForeignKey(Curators, on_delete=models.CASCADE, null=True)
    groupId = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)






