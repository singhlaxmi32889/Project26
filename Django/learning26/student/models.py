from django.db import models
 
# Create your models here.
class student(models.Model):
   student_name= models.CharField(max_length=100)
   student_age= models.IntegerField()
   student_city= models.CharField(max_length=60)
   student_email= models.EmailField(null=True)
   
   class Meta:
      db_table="student"

class product(models.Model):
   product_name= models.CharField(max_length=100)
   product_price= models.IntegerField()
   product_description= models.CharField(max_length=60)
   product_stock= models.IntegerField(null=True)
   product_color= models.CharField(max_length=60,null=True)
   product_status= models.BooleanField(default=True)
   
   
   class Meta:
      db_table="product"

class branch(models.Model):
    branch_name= models.CharField(max_length=100)
    branch_subject= models.CharField(max_length=100)
    branch_credit= models.IntegerField()
    branch_duration= models.IntegerField()
    branch_fee= models.IntegerField()
    
    class Meta:
        db_table = "branch"     