from django.urls import path
from . import views
urlpatterns = [
	path('',views.index,name = 'home'),
	path('timetable/', views.timetable , name='timetable'),
	path('addmoney',views.addmoney , name = 'addmoney'),
	path('pay',views.pay , name = 'pay')
]