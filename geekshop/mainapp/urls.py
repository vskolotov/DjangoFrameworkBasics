from django.urls import path

import mainapp.views as views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='index'),
    path('<int:pk>/', views.products, name='category'),
]
