from django.urls import path
from webapp.views import index_view, task_create_view, task_delete_view, task_view

urlpatterns = [
    path('', index_view),
    path('task/add/', task_create_view),
    path('task/delete/', task_delete_view),
    path('task/<int:pk>/', task_view)
]
