from django.urls import path,include
from . import views

app_name="lession04"
urlpatterns = [
        path('upload/', views.fileUploaderView, name='fileUploaderView'),
        path('animal/', views.indexAnimal, name='indexAnimal'),
                
]
