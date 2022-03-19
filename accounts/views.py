from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return render(request, self.template_name, {'form': form})
