from django.shortcuts import redirect, render
from .forms import UserRegisterForm

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return(redirect('tops_app:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)