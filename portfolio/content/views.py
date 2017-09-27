from .models import Article, Work
from django.http import Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home (request):
	menu = Article.objects.all() #HARDCODED - BUSCAR UMA ALTERNATIVA , TA AQUI SO PARA DEMARCAR
	lista_artigos = Article.objects.all() #Faz a queary dos Artigos
	paginator = Paginator(lista_artigos, 2) #Cria um objeto paginator é passa a queary para uma função chamada Paginator expecificando quantos objetos da queary vc quer por pagina.
	
	trabalhos_feitos = Work.objects.all() # Chama o objeto 'Work' que é uma tabela contida em models para o portfolio
	

	page = request.GET.get('page')  
	try:
		conteudo = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		conteudo = paginator.page(1)
	except EmptyPage:
		 # If page is out of range (e.g. 9999), deliver last page of results.
		conteudo = paginator.page(paginator.num_pages)

	context = {'conteudo_artigo': conteudo, 'menu':menu,'trabalhos':trabalhos_feitos}
	return render(request, 'base.html', context)


def artigos(request,id_pagina_artigo): #Pega o ID capturado pelo Regex da url e usa como elemento para achar determinado Artigo
	try:
		materia = Article.objects.get(id=id_pagina_artigo)
	except ObjectDoesNotExist:
		raise Http404
	return render(request, 'artigo.html', {'teste': materia})

def portfolio(request): #renderiza a pagina de portifolio em sí 
	trabalhos_feitos = Work.objects.all()
	context = {'trabalhos': trabalhos_feitos}
	return render(request, 'portfolio.html', context)