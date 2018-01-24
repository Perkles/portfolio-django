from .models import Post
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def Blog (request):
	post = Post.objects.all()

	paginator = Paginator(post, 1) # Show 1 post per page
	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	
	context = {'post':post, 'contacts':contacts}
	return render(request, 'home.html', context)

def Articles(request,id_pag): #Pega o ID capturado pelo Regex da url e usa como elemento para achar determinado Artigo
	try:
		article_content = Post.objects.get(id=id_pag) #Trabalhar aqui para que fique dinamico. quando deleta artigos ele continua a soma.
	except ObjectDoesNotExist:
		return render(request, '404.html')

	return render(request, 'article.html', {'article_content': article_content})