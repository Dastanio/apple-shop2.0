from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Products
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect

from django.urls import reverse



def main(request):
	return render(request, 'shop/main.html')

def about(request):
	return render(request, 'shop/about.html')

def email(request):

	if request.method == 'POST':
		message = request.POST['message']
		gmail = request.POST['gmail']
		send_mail('gmail почта клиента:  ' + gmail, 
		 'Текст сообщения от клиента:  ' + message, 
		 settings.EMAIL_HOST_USER,
		 ['dassu8457@gmail.com'], # <--- вот сдесь ты едешь 2 аккаунт  
		 fail_silently=False)


		messages.success(request, ('Ваш заказ успешно принят, доставщик свами свяжется'))
		return redirect('email')

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

