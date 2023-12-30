from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import ToDo


class ToDoListView(ListView):
    model = ToDo  # Lembrar de manter o contexto, ou seja, o nome do template deve ser noi me da função + _ + list, tudu minúsculo


class ToDoCreateView(CreateView):
    model = ToDo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class ToDoUpdateView(UpdateView):
    model = ToDo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class ToDoDeleteView(DeleteView):
    model = ToDo
    success_url = reverse_lazy("todo_list")


class ToDoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.mark_has_completed()
        return redirect("todo_list")
