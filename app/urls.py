from django.urls import path
from . import views

urlpatters = [
    path('index', views.index, name="index"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('login', views.login, name="login"),
    path('submeterProblema', views.submeterProblema, name= "submeterProblema"),
    path('painel', views.painel, name="painel"),
    path('perfil', views.perfil, name="perfil"),
    path('editar/<int:id>', views.editar, name="editar")
]