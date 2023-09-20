from django.db import models

# Create your models here.

class NewsModel(models.Model):
    title=models.CharField(max_length=80,default='')
    body=models.TextField()
    status=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title