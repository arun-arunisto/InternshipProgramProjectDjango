from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Applicants(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    dob = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    mail = models.EmailField(max_length=150, unique=True)
    qualification = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images')
    address = models.TextField()
    objective = models.TextField()

    def __str__(self):
        return self.name

#adding is_submitted() method within User model
User.add_to_class("is_submitted", lambda user:Applicants.objects.filter(user=user).exists())
