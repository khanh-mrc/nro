from django.db import models
class Usera(models.Model):
    username = models.CharField(max_length=200, null=True)
    #phone = models.CharField(max_length=20, null=True)
    #email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.username

# Create your models here.
