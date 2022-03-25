from django.urls import path,include
from . import views

app_name="lession02"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:person_id>', views.detail, name='detail'),
    path('form-input/', views.formInput, name='formInput'),
    path('thankyou/', views.thankYou, name='thankYou'),

]