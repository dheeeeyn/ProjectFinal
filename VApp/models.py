from django.db import models

class User(models.Model):
	GENDER = (
			('Male', 'Male'),
			('Female', 'Female'),
			)
	YName = models.TextField(default="", null=True)
	YAddress = models.TextField(default="", null=True)
	Ybday = models.DateTimeField(default='', null=True)
	YContact = models.CharField(default="", max_length=11)
	YGender = models.TextField(default="", null=True, choices=GENDER)
	email= models.TextField(default="", null=True)
	password1= models.TextField(default="", max_length=15, null=True)
	
	def _str_(self):
		return self.YName

	class meta:
		db_table = "User"

	

#volunteer

class Volunteer(models.Model):
	BRANCH = (
			('Bayan', 'Bayan'),
			('Area 1', 'Area 1'),
			('Paliparan 2', ' Paliparan 2'),
			)
	SCHED = (
			('Monday', 'Monday'),
			('Wednesday', 'Wednesday'),
			('Friday', 'Friday'),
			('Saturday', 'Saturday'),
			)
	VolId = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
	VTask = models.TextField(default='',null=True) #Task
	VSched = models.TextField(default='', null=True, choices=SCHED)
	VSched_create = models.DateTimeField(auto_now_add=True, null=True)
	VBranch = models.TextField(default='',null=True, choices=BRANCH)
	VStatus = models.TextField(default=None,null=True)

	def _str_(self):
		return self.VTask

	class meta:
		db_table = "Volunteer"


# Donation
class Donation(models.Model):
	BRANCH = (
			('Bayan', 'Bayan'),
			('Area 1', 'Area 1'),
			('Paliparan 2', ' Paliparan 2'),
			)
	DoId = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
	DFood = models.TextField(default='')
	DQuantity = models.IntegerField(default='',null=True,)
	DBranch = models.TextField(default='',null=True, choices=BRANCH)
	DSched_create = models.DateTimeField(auto_now_add=True, null=True)
	DStatus = models.TextField(default=None)
	class meta:
		db_table = "Donation"

#Profile Ticket
class Profile(models.Model):
	YProfile = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
	YTask = models.TextField(default='', null=True)
	YWhen = models.DateTimeField(default='', null=True)
	YWhere = models.TextField(default='', null=True)
	class meta:
		db_table = "My_Profile"

# Contact Us
class Contact(models.Model):
	name = models.TextField(default="", null=True)
	email = models.TextField(default="", null=True)
	message = models.TextField(default="", null=True)


# class Volunteer(models.Model):
# 	pass

# class Item(models.Model):
# 	VolId = models.ForeignKey(Volunteer, default=None, on_delete=models.CASCADE)
# 	text = models.TextField(default='') #interest
# 	Sched= models.TextField(default='')
# 	schedT= models.TextField(default='')



	# pass
# Create your models here.
