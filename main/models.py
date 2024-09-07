from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    url = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.url