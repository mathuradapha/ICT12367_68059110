from django.urls import path
from . import views

urlpatterns = [

    path('',views.home),
    path('form/',views.form),
    path('delete/<int:id>/',views.delete),
    path('edit/<int:id>/',views.edit),

]