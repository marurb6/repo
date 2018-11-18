from django.urls import path
from . import views

urlpatterns = [ 
	path('', views.bazowy, name='bazowy'), 			
	path('home/', views.home, name='home'), 
	path('maria/', views.maria, name='maria'), 
	path('about/', views.about, name='about'),
]