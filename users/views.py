from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.views.generic import CreateView
from .forms import UserRegisterForm


def logout_view(request):
    logout(request)
    return redirect("index")


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
