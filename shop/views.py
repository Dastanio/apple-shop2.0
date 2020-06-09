from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Products, Comments

from django.urls import reverse



def main(request):
	return render(request, 'shop/main.html')

def about(request):
	return render(request, 'shop/about.html')

def email(request):
	return render(request, 'shop/email.html')

#apple
def applephone(request):
	latest_articles_list = Products.objects.order_by('-pub_date')[:5]
	return render(request, 'shop/products/applephone.html', {'latest_articles_list': latest_articles_list})


def detail(request, id_iphone):
	try:
		a = Products.objects.get( id = id_iphone)
	except:
		raise Http404('Товар не найден!')

	latest_comments_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'shop/products/iphonedetail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, id_iphone):
	try:
		a = Products.objects.get( id = id_iphone)
	except:
		raise Http404('Товар не найден!')

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('shop/products/iphonedetail.html', args = (a.id,)) )

