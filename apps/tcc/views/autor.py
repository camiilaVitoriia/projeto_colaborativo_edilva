from apps.tcc.models import Autor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class AutorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'ultimo_nome', 'foto']

    success_message = 'Autor cadastrado com sucesso!'

    template_name = "cadastros/form.html"

    success_url = reverse_lazy("listar-autores")


    def get_context_data(self, **kwargs):

        context = super(CreateView, self).get_context_data(**kwargs)

        context['titulo'] = 'Autores'

        context['descricao'] = 'Cadastro de Autor(a)'
        return context


    def form_valid(self, form):

        url = super().form_valid(form)
        return url


class AutorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'ultimo_nome', 'foto']

    success_message = 'Autor(a) atualizado com sucesso!'

    template_name = "cadastros/form.html"

    success_url = reverse_lazy("listar-autores")


    def get_context_data(self, **kwargs):

        context = super(UpdateView, self).get_context_data(**kwargs)

        context['titulo'] = 'Autores'

        context['descricao'] = 'Editar Autor(a)'

        context['botao'] = 'Salvar'
        return context


    def form_valid(self, form):

        url = super().form_valid(form)
        return url


class AutorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = Autor
    success_message = 'Autor(a) excluído com sucesso!'

    template_name = "cadastros/form-excluir.html"

    success_url = reverse_lazy("listar-autores")


class AutorList(ListView):
    model = Autor

    template_name = "listas/autores.html"

