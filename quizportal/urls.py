from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('dashboard/', user_views.dashboard_view, name='dashboard'),
    path('', user_views.login_view, name='home'),
   path('quiz/', include(('quiz.urls', 'quiz'), namespace='quiz')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)