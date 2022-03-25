from django.urls import  include,path

from . import views

app_name="lession05"


urlpatterns = [
    path('send-mail/', views.sendMail, name='send-mail'),
    path('cache', views.get_products_cached, name='cached'),


]