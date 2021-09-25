
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as users_views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('register/', users_views.register, name="register-page"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout-page"),
    path('profile/', users_views.profile, name="profile-page"),
    path('', blog_views.main, name='main-page'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

