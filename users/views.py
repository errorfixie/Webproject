from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .forms import CreateUserForm, UserLoginForm, LikebooksForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

class CreateUserView(CreateView):
    template_name = 'users/join_form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('home')

    def likebookchoice(request):
        context = {}
        context['form'] = LikebooksForm()
        return render(request, "Join_form.html", context)

class CustomLoginView(LoginView):
    template_name = 'users/login_form.html'
    form_class = UserLoginForm

@login_required
def update(request):
    if request.method == 'Post':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:people', request.user.username)
        else:
            user_change_form = CustomUserChangeForm(instance=request.user)
            return render(request, 'usersa/update.html',{'user_change_form':user_change_form})