from django.urls import path
from forms import views
from django.conf.urls import url


urlpatterns=[
	path('add_data',views.add_data,name='add_data'),
	path('view_data',views.list_data,name='list_data'),
]