from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages as msg
from .forms import LearnerForm
from blog.models import CareerInfo
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import Tutor




def register(request):
    if request.method=='POST':
        try:
            form=LearnerForm(request.POST)
            if form.is_valid:
                form.save()
                msg.success(request, f'The Account is created ')
                return redirect('login-page')
        except:
            pass
    else:
        form=LearnerForm()

    return render(request, 'users/register.html', {'form':form})
    
@login_required
def profile(request):
    context={'Posts':CareerInfo.objects.all()}
    return render(request, 'users/learner.html', context)
    
@login_required
def tutor(request):
    context={"Tutors": Tutor.objects.all()}
    return render(request, 'users/tutor_profile.html', context)

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "users/password_reset_email.txt"
                    c = {
                                "email":user.email,
                                'domain':'127.0.0.1:8000',
                                'site_name': 'Website',
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                        }
                    email = render_to_string(email_template_name, c)
                    try:send_mail(subject, email, 'eddymalegale@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError: return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
        
    form = PasswordResetForm()
    return render(request=request, template_name="users/password_rest.html", context={"password_reset_form":form})

# Create your views here.
