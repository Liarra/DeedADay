from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hardness(models.Model):
	name=models.CharField(max_length=20)
	
	def __unicode__(self):
		 return self.name
	
class Tag(models.Model):
	name=models.CharField(max_length=50)
	
	def __unicode__(self):
		 return self.name

class Deed(models.Model):
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=500)
	hardness=models.ForeignKey(Hardness)
	tags=models.ManyToManyField(Tag)
	image=models.CharField(max_length=256)
	link=models.CharField(max_length=256, blank=True)
		
	def __unicode__(self):
		 return self.name

class DeedUser(User):
	deeds=models.ManyToManyField(Deed)
	ext_id=models.CharField(max_length=50)
	
