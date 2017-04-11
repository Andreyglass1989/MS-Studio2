"""MS_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.http import HttpResponse, Http404
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about-ms-studio/$', views.about_ms_studio, name = 'about'),
    url(r'^contacts/$', views.contacts, name = 'contacts'),
    url(r'^projects/', include ('projects_home.urls')),
    url(r'^design_interera/', include ('design_interera.urls')),
    url(r'^public/', include ('public_building.urls')),
    url(r'^partner/', views.partner, name='partner'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)