from django.db import models

class info(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	message = models.CharField( max_length=1000, null=True, blank=True)
 


	

# Create your models here.
