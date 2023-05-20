from decimal import Decimal

from django.db import models
from datetime import timedelta
from django.core.validators import MaxLengthValidator,MinLengthValidator
# Create your models here.
class Departments(models.Model):
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
    building = models.CharField(max_length=2,choices=day_CHOICES,default=First)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# class Diseases(models.Model):
#     name = models.CharField(null=False,max_length=100)
#     severity = models.IntegerField(null=False,max_length=10,default=1)
#     def __str__(self):
#         return self.name
class Doctors(models.Model):
    name = models.CharField(null=False,max_length=100)
    number = models.CharField(null=False,max_length=13)
    salary = models.DecimalField(decimal_places=2, max_digits=10,default=1)
    surname = models.CharField(null=False,max_length=100)
    premium=models.DecimalField(decimal_places=2, max_digits=10,default=1)
    def __str__(self):
        return self.name
class Examinations(models.Model):
    name = models.CharField(null=False, max_length=100)
    # Monday='Mo'
    # Tuesday = 'Tu'
    # Wednesday = 'We'
    # Thursday = 'Th'
    # Friday = 'Fr'
    # Saturday = 'Sa'
    # Sunday = 'Su'
    # day_CHOICES=[
    #     (Monday,'Monday'),
    #     (Tuesday, 'Tuesday'),
    #     (Wednesday, 'Wednesday'),
    #     (Thursday, 'Thursday'),
    #     (Friday, 'Friday'),
    #     (Saturday, 'Saturday'),
    #     (Sunday, 'Sunday')
    # ]
    # DayOfWeek = models.CharField(max_length=2,choices=day_CHOICES,default=Monday)
    # starttime = models.TimeField(auto_now=False,blank=True,null=True)
    # endtime = models.TimeField(auto_now=False,blank=True,null=True)
    # def save(self,*args,**kwargs):
    #     if self.starttime>self.endtime:
    #         self.endtime=self.starttime
    #     else:
    #         pass
    #     super(Examinations,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
class Wards(models.Model):
    name = models.CharField(null=False, max_length=100)
    places= models.DecimalField(decimal_places=2, max_digits=10,default=1)
    departamentid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
class DoctorsExaminations(models.Model):
    startime=models.TimeField()
    endtime=models.TimeField()
    doctorid=models.ForeignKey(Doctors,on_delete=models.CASCADE,null=True)
    examinationod=models.ForeignKey(Examinations,on_delete=models.CASCADE,null=True)
    wardid=models.ForeignKey(Wards,on_delete=models.CASCADE,null=True)
    def save(self,*args,**kwargs):
        if self.startime>self.endtime:
         self.endtime=self.startime
        else:
         pass
         super(DoctorsExaminations,self).save(*args,**kwargs)
class Sponsors(models.Model):
    name = models.CharField(null=False, max_length=100)
class Donation(models.Model):
    amount=models.DecimalField(max_digits=100,decimal_places=2,validators=[MinLengthValidator(Decimal('0.00'))])
    date=models.DateField()
    departamentid=models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    sponsorid=models.ForeignKey(Sponsors,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.date

