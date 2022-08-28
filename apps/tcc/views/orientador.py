from apps.tcc.models import Orientador
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Orientador
    fields = ['nome', 'ultimo_nome', 'link_do_curriculo']
    success_message = 'orientador cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-orientadores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'orientadores'
        context['descricao'] = 'Cadastro de orientador(a)'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Orientador
    fields = ['nome', 'ultimo_nome', 'link_do_curriculo']
    success_message = 'orientador(a) atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-orientadores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'orientadores'
        context['descricao'] = 'Editar orientador(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Orientador
    success_message = 'orientador(a) excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-orientadores")

class OrientadorList(ListView):
    model = Orientador
    template_name = "listas/orientadores.html"
