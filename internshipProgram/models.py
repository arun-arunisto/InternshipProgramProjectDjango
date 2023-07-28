from django.db import models

# Create your models here.
class Applicants(models.Model):
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

