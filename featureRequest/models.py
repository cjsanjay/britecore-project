from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    client_a='A'
    client_b='B'
    client_c='C'
    policy='P'
    bill='B'
    claim='C'
    report='R'
    client_choice=((client_a,'Client A'),(client_b,'Client B'),(client_c,'Client C'),)
    prod_choice=((policy,'Policies'),(bill,'Billing'),(claim,'Claims'),(report,'Reports'))
    
    #fields decalaration   
    title = models.CharField(max_length=200)    
    client = models.CharField(max_length=1,choices=client_choice)
    client_priority=models.IntegerField()
    description = models.TextField()    
    target_date=models.DateField(auto_now=False, auto_now_add=False)
    ticket_url=models.URLField()
    prod_area=models.CharField(max_length=1,choices=prod_choice)   

    def publish(self):       
        self.save()

    def __str__(self):
        return self.title             
