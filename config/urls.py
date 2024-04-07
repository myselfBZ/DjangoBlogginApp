from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import log_out
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', log_out, name='logout'),
]

if settings.DEBUG:

     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


