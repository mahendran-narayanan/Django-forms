from django.urls import path
from forms import views
from django.conf.urls import url
from forms.views import get_name
urlpatterns=[
	path('home.html',views.home,name="home"),
	url(r'^$',views.get_name,name="getname"),
	path('thanks/',views.thanks,name="thanks"),
	path('add_car',views.add_car,name='add_car'),
	path('cars',views.car_list,name='car_list'),
]