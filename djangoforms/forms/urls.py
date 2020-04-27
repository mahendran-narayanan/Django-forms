from django.urls import path
from forms import views
from django.conf.urls import url


urlpatterns=[
	path('add_data',views.add_data,name='add_data'),
	path('add_car',views.add_car,name='add_car'),
	path('cars',views.car_list,name='car_list'),
	path('car/<int:car_billing_number>',views.car_details,name='car_details'),
]