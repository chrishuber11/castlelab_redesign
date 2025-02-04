from django.urls import path,re_path
from website import views
urlpatterns = [
	re_path(r'^',views.index,name='index'),
	]

