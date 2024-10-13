from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class RegistroView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('index') 

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response