from django.db import models
from tinymce import models as tinymce_models


class Article(models.Model):
	titulo = models.CharField(max_length=200)
	photo = models.FileField(upload_to='static', null=True, blank=True) #procurar como fica em produção
	autor = models.CharField(max_length=30)
	corpo = tinymce_models.HTMLField(null=True, blank=True) #Tinymce field
	data = models.DateField()
	tag = models.CharField(max_length=30)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-data'] #Ordena minha classe artigo no queryset por data


class Work(models.Model):
	nome = models.CharField(max_length=200)
	imagem = models.FileField(upload_to='static', null=True, blank=True) #procurar como fica em produção
	descricao = models.CharField(max_length=200)
	fim = models.DateField()

	def __str__(self):
		return self.nome

	class Meta:
		ordering = ['-fim'] #Ordena minha classe artigo no queryset por data
