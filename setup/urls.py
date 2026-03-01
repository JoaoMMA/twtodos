from django.contrib import admin
from django.urls import path, include
from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
    IndexView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("list", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>/", TodoCompleteView.as_view(), name="todo_complete"),
    path("usuarios/", include("users.urls")),
]
