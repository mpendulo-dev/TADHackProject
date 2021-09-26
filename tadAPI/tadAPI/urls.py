
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views as blog_views
from users import views as users_views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path('register/', users_views.register, name="register-page"),
    path('tutors/' ,users_views.tutor, name ="tutor-page"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout-page"),
    path('profile/', users_views.profile, name="profile-page"),
    path('', blog_views.main, name='main-page'),
    path('admin/', admin.site.urls),
    path('^', include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_rest.html'), name='passwordReset-page'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),      

]

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

