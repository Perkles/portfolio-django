from django.db import models
from tinymce import models as tinymce_models

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=30)
	body = tinymce_models.HTMLField(null=True, blank=True) #Tinymce field
	data = models.DateField()
	tag = models.CharField(max_length=30)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-data']
