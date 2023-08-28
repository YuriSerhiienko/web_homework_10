from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, context={'form': self.form_class()})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
        return render(request, self.template_name, context={'form': form})