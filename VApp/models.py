from django.db import models

class Volunteer(models.Model):
	pass

class Item(models.Model):
	VolId = models.ForeignKey(Volunteer, default=None, on_delete=models.CASCADE)
	text = models.TextField(default='')


	# pass
# Create your models here.
