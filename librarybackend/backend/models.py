from email.policy import default
from pickle import TRUE
from django.db import models
# Create your models here.
class Upload(models.Model):
    description = models.CharField(max_length= 600, default='/', blank=True, null=True)
    img = models.ImageField(upload_to = "Images/", blank=True, default="Empty")