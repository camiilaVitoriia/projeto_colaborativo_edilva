from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/', PasswordChangeView.as_view(template_name='cadastros/mudar-senha.html'), name='mudar-senha'),
    path('criar/usuario/', UsuarioCreate.as_view(), name='criar-usuario'),
    path('editar/usuario/<int:pk>', UsuarioUpdate.as_view(), name='editar-usuario'),
    path('listar/usuarios/', UsuarioList.as_view(), name='listar-usuarios'),
    path('deletar/usuario/<int:pk>', UsuarioDelete.as_view(), name='deletar-usuario'),
]