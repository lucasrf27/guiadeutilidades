from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home2'),
    path('parceiro/', views.parceirosview, name='parceiro2'),
    path('addparceiro/', views.parceiros_create, name='add_parceiro2'),
]
