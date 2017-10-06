from django.db import models
from tinymce import models as tinymce_models


class SobreMim(models.Model):
	nome = models.CharField(max_length=200)
	foto = models.FileField(upload_to='static', null=True, blank=True) #procurar como fica em produção
	descricao = tinymce_models.HTMLField(null=True, blank=True) #Tinymce field

	def __str__(self):
		return self.nome