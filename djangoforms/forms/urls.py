from django.urls import path
from forms import views

urlpatterns=[
	path('home.html',views.home,name="home"),
]