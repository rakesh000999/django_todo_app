from django.db import models

# Create your models here.
class User(models.Model):
    # age = models.IntegerField(default=20)
    # monthly_salary = models.BigIntegerField()
    
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    