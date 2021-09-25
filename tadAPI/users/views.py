from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages as msg
from .forms import UserForm
from blog.models import CareerInfo




def register(request):
    if request.method=='POST':
        try:
            form=UserForm(request.POST)
            if form.is_valid:
                form.save()
                msg.success(request, f'The Account is created ')
                return redirect('login-page')
        except:
            pass
    else:
        form=UserForm()

    return render(request, 'users/register.html', {'form':form})
    
@login_required
def profile(request):
    context={'Posts':CareerInfo.objects.all()}
    return render(request, 'users/profile.html', context)

# Create your views here.
