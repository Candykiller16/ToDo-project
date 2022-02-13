from django.urls import path
from todo.views import AboutView, TaskView, UpdateTaskView, DeleteTaskView, CreateTaskView

urlpatterns = [
    path('', TaskView.as_view()),
    path('todo/update_task/<int:pk>', UpdateTaskView.as_view(), name='update'),
    path('todo/delete_task/<int:pk>', DeleteTaskView.as_view(), name='delete'),
    path('todo/create_task/', CreateTaskView.as_view(), name='create'),
]