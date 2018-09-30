from .models import Project
from django.shortcuts import render

def Portfolio(request):
	project = Project.objects.all()

	context = {'project':project}
	return render(request, 'portfolio.html', context)

