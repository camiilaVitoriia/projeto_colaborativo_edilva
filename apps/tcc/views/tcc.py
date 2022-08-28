from apps.tcc.models import Tcc
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class TccCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tcc
    fields = ['titulo', 'autor', 'orientador', 'curso', 'ano_documento', 'resumo', 'arquivo_documento', 'palavras_chave']
    success_message = 'tcc cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-tccs")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'tccs'
        context['descricao'] = 'Cadastro de tcc'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tcc
    fields = ['titulo', 'autor', 'orientador', 'curso', 'ano_documento', 'resumo', 'arquivo_documento', 'palavras_chave']
    success_message = 'tcc atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-tccs")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'tccs'
        context['descricao'] = 'Editar tcc'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tcc
    success_message = 'tcc excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar-tccs")

class TccList(ListView):
    model = Tcc
    template_name = "index.html"

class TccDetail(DetailView):
    model = Tcc
    template_name = "detalhe/tcc.html"

class Index(ListView):
    model = Tcc
    template_name = "index.html"
