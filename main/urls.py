from django.urls import path
from django.conf import settings
from . import views


app_name = 'main'
urlpatterns = [
	path('index/', views.IndexView.as_view(), name = 'index')
]