from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cars(models.Model):
    make=models.CharField(max_length=200)
    mileage=models.PositiveIntegerField()
    no_of_owners=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    address=models.CharField(max_length=300)
    year=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.make
 
