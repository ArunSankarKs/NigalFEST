from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Awards(models.Model):
    Title=models.CharField(max_length=30)
    img=models.ImageField(upload_to='media')

class Workshop(models.Model):
    title=models.CharField(max_length=30)
    title_img=models.ImageField(upload_to='media')
    descrip=models.CharField(max_length=30)
    full_img=models.ImageField(upload_to='media')
    venue=models.CharField(max_length=30)
    time=models.DateField()
    conducted_by=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)

class Event(models.Model):
    title=models.CharField(max_length=30)
    Title_img=models.ImageField(upload_to='media')
    Full_img=models.ImageField(upload_to='media')
    Description=models.CharField(max_length=30)
    Venue=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    Date=models.DateField()
    Conducted_by=models.CharField(max_length=30)


class Members (models.Model):
    Name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='media')

class Home(models.Model):
    img=models.ImageField(upload_to='media')

