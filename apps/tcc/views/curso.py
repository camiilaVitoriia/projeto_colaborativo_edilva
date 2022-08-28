from apps.tcc.models import Curso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curso
    fields = ['nome', 'modalidade']
    success_message = 'curso cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cursos")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'cursos'
        context['descricao'] = 'Cadastro de curso'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curso
    fields = ['nome', 'modalidade']
    success_message = 'curso atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cursos")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'cursos'
        context['descricao'] = 'Editar curso'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Curso
    success_message = 'curso excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-cursos")

class CursoList(ListView):
    model = Curso
    template_name = "listas/cursos.html"
