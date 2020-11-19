from django.conf.urls import url
from login import views
from django.urls import path
app_name = 'login'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_log,name='login'),
]
