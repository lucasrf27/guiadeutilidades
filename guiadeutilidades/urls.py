from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls'), name='home1'),
    path('accounts/', include('accounts.urls'), name='accounts1'),
]
