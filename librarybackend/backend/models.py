from django.db import models

class Image(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length= 600)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)