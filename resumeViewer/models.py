from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    resume=models.FileField(upload_to='uploads/')
    feedback=models.CharField(max_length=5000,blank=True)

    def __str__(self) -> str:
        return f"{self.id}"