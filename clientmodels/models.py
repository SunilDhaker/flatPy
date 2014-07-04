from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Venders(models.Model):
	name = models.CharField(max_length=50)
	vender_type = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	is_verified = models.BooleanField() 
	# avatar = models.ImageField(upload_to='/images/')
	def __unicode__(self):
		return self.name


class Bill(models.Model):
	venders = models.ForeignKey(Venders)
	consumer = models.ForeignKey(User)
	amount = models.CharField(max_length=50)
	created_at = models.DateTimeField(default=datetime.now())
	is_paid = models.BooleanField()
	tax = models.CharField(max_length=50)