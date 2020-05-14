from django.db import models

# Create your models here.
class Class12(models.Model):
    title = models.CharField(max_length=50)
    video=models.FileField(upload_to='class12/videos')


    def __str__(self):
        return self.title
class Class11(models.Model):
    title = models.CharField(max_length=50)
    video=models.FileField(upload_to='class11/videos')


    def __str__(self):
        return self.title
        