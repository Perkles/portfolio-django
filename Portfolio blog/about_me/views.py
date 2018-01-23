from content.models import Article
from .models import SobreMim
from django.shortcuts import render

def sobremim_page(request):
	menu = Article.objects.all()
	bio = SobreMim.objects.all()
	context = {'bio': bio, 'menu':menu}
	return render(request, 'sobremim.html', context)
