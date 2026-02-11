from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    class Meta:
        db_table = "course"
    def __str__(self):
        return self.name

class Studentf(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
        db_table = "studentf"
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()    
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100) 
    class Meta:
        db_table = "teacher" 
    def __str__(self):
        return self.name

class Productf(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    class Meta:
        db_table = "productf"
    def __str__(self):
        return self.name