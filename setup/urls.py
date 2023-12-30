from django.contrib import admin
from django.urls import path

from todos.views import (
    ToDoListView,
    ToDoCreateView,
    ToDoUpdateView,
    ToDoDeleteView,
    ToDoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ToDoListView.as_view(), name="todo_list"),
    path("create/", ToDoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", ToDoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", ToDoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", ToDoCompleteView.as_view(), name="todo_complete"),
]
