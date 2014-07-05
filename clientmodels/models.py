from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Venders(models.Model):
	brand = models.CharField(max_length=50)
	place = models.CharField(max_length=50) 
	image = models.ImageField(upload_to='images' , default='images/2.jpg')
	def __unicode__(self):
		return self.branch



class Bill(models.Model):
	venders = models.ForeignKey(Venders)
	consumer = models.ForeignKey(User)
	amount = models.CharField(max_length=50)
	created_at = models.DateTimeField(default=datetime.now())
	is_paid = models.BooleanField()
	tax = models.CharField(max_length=50)