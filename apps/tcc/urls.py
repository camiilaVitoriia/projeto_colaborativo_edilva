from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view() , name='index'),

    path('criar/autor/', AutorCreate.as_view(), name='criar-autor'),
    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name='editar-autor'),
    path('deletar/autor/<int:pk>/', AutorDelete.as_view(), name='deletar-autor'),
    path('listar/autores/', AutorList.as_view(), name='listar-autores'),

    path('criar/curso/', CursoCreate.as_view(), name='criar-curso'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar-curso'),
    path('deletar/curso/<int:pk>/', CursoDelete.as_view(), name='deletar-curso'),
    path('listar/cursos/', CursoList.as_view(), name='listar-cursos'),

    path('criar/orientador/', OrientadorCreate.as_view(), name='criar-orientador'),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name='editar-orientador'),
    path('deletar/orientador/<int:pk>/', OrientadorDelete.as_view(), name='deletar-orientador'),
    path('listar/orientadores/', OrientadorList.as_view(), name='listar-orientadores'),

    path('criar/tcc/', TccCreate.as_view(), name='criar-tcc'),
    path('editar/tcc/<int:pk>/', TccUpdate.as_view(), name='editar-tcc'),
    path('deletar/tcc/<int:pk>/', TccDelete.as_view(), name='deletar-tcc'),
    path('listar/tccs/', TccList.as_view(), name='listar-tccs'),
    path('detalhar/tcc/<int:pk>', TccDetail.as_view(), name='detalhar-tcc'),
]
