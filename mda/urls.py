from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from initiatives import views
from pmanager import pviews
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('user/', pviews.userindex, name='user'),
    path('admin/', include('initiatives.urls')),
    path('pmanager/', include('pmanager.urls')),
    path('sultan/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
