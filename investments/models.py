from django.db import models

# Create your models here.
class Investment(models.Model):
    company = models.CharField(max_length=250)
    quantity = models.IntegerField()
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company