from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name = 'main'),
	path('about/', views.about, name = 'about'),
	path('email/', views.email, name = 'email'),
	path('applephone/', views.applephone, name = 'applephone'),
	path('applephone/<int:id_iphone>', views.detail, name = 'iphonedetail'),
	path('applephone/<int:id_iphone>', views.leave_comment, name = 'leave_comment'),
]