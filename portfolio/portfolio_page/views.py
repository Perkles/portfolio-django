from content.models import Article
from .models import Portfolio
from django.shortcuts import render

def portfolio_pagina(request):

	menu = Article.objects.all()
	escopo = Portfolio.objects.all()
	context = {'escopo':escopo,'menu':menu}

	return render(request, 'portfolio.html', context)
	