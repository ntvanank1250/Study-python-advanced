from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lession01/',include('lession01.urls')),
    path('lession02/',include('lession02.urls')),
    path('lession04/',include('lession04.urls')),
    path('lession05/',include('lession05.urls')),
]