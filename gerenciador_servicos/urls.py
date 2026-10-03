from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrocliente/', views.cadastrocliente, name='cadastrocliente'),
    path('cadastro2/', views.cadastro2, name='cadastro2'),
    path('consultacliente/', views.consultacliente, name='consultacliente'),
    path('consulta2/', views.consulta2, name='consulta2'),
    path('excluir1/<int:id>', views.excluir1, name='excluir1'),
    path('editar1/<int:id>', views.editar1, name='editar1')
]