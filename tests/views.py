from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import DDD

# Create your views here.



def post_detail(request, post_id):
	obj = get_object_or_404(DDD, id=post_id)
	context = {
		"post_detail" : obj,
	}
	
	return render(request, 'detail.html', context)



def post_list(request):
	obj_list = DDD.objects.all()
	context ={
		"post_list" : obj_list
	}

	return render(request, 'list.html', context)


