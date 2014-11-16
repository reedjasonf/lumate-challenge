from django.db import models

# Create your models here.
class Signature(models.Model):
	first_name = models.CharField(max_length=192)
	last_name = models.CharField(max_length=192)
	sign_date = models.DateTimeField('date signed')

	def __str__(self):
		return self.first_name+" "+self.last_name

