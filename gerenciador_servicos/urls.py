from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrocliente/', views.cadastrocliente, name='cadastrocliente'),
    path('consultacliente/', views.consultacliente, name='consultacliente'),
    path('editar1/<int:id>/', views.editar1, name='editar1'),
    path('excluir1/<int:id>/', views.excluir1, name='excluir1'),
    path('cadastro2/', views.cadastro2, name='cadastro2'),
    path('consulta2/', views.consulta2, name='consulta2'),
    path('editar2/<int:id>/', views.editar2, name='editar2'),
    path('excluir2/<int:id>/', views.excluir2, name='excluir2'),