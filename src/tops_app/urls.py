from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'tops_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
 ]