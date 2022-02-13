from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import FormView
from members.forms import MyUserCreationForm


class UserRegistrationView(FormView):
    template_name = 'register/register.html'
    form_class = MyUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
