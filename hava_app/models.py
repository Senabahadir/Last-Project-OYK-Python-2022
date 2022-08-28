from django.db import models
from datetime import datetime

class Hava(models.Model):

    # title = models.CharField(max_length=100
 
    day = models.DateTimeField(default=datetime.now)
    date = models.DateTimeField(default=datetime.now ,blank=True )
    derece = models.IntegerField()
    description = models.TextField(max_length=1000,blank=True)
    sehir = models.TextField(max_length=100, blank=True)
    

    def __str__(self):
        return self.description