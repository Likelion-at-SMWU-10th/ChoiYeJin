from django.db import models
from django.utils import timezone

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:10]