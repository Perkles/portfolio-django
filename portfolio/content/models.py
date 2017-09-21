from django.db import models


class Article(models.Model):
	titulo = models.CharField(max_length=200)
	corpo = models.TextField()
	data = models.DateField()

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-data'] #Ordena minha classe artigo no queryset por data