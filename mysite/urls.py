from django.contrib import admin
from django.urls import path, include
from myweb import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('myweb.urls')),
    path('admin/', admin.site.urls),


]
