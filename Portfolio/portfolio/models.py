from django.db import models
from tinymce import models as tinymce_models


class Project(models.Model):
	
	image =  models.ImageField(upload_to='media', null=True, blank=True)	
	name = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	description = tinymce_models.HTMLField(null=True, blank=True) #Tinymce field
	tecnology = models.CharField(max_length=200)
	data = models.DateField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-data']
