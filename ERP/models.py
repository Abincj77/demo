from django.db import models

# Create your models here.

class Employer(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField()
    phone = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
   
