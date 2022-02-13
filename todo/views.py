from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, FormView
from .models import Task

# Create your views here.

class AboutView(TemplateView):
    template_name = 'base.html'


class TaskView(LoginRequiredMixin, ListView):
    """
    Отображает все таски на странице
    """
    model = Task
    template_name = 'base.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title']
    template_name = 'update_task.html'
    success_url = '/'

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/'


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create_task.html'
    fields = ['title']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




