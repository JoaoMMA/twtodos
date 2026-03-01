from django.shortcuts import get_object_or_404, redirect
from .models import Todo
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    TemplateView,
)
from django.urls import reverse_lazy
from .forms import TodoForm
from django.contrib.auth.mixins import LoginRequiredMixin  # Importe o Mixin


class IndexView(TemplateView):
    template_name = "todos/index.html"


# 1. LISTA: Só vê as tarefas dele
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


# 2. CRIAÇÃO: O dono da tarefa é setado automaticamente como o user logado
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Vincula o usuário logado à tarefa
        return super().form_valid(form)


# 3. EDIÇÃO: get_queryset garante que ele não edite IDs de outros
class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


# 4. EXCLUSÃO: get_queryset garante que ele não delete IDs de outros
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


# 5. CONCLUSÃO: Filtramos o objeto diretamente pelo usuário no get_object_or_404
class TodoCompleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        # Aqui o segurança é o filtro adicional user=request.user
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo.mark_as_complete()
        return redirect("todo_list")
