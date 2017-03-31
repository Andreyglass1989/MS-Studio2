from django.conf.urls import url, include
#from django.conf.urls.defaults import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects_home'
urlpatterns = [
    url(r'^$' , views.projects_house, name='projects_house'),
    #url(r'^(?P<pk>\d+)/$' , views.design_interera, name='design_interera'),
    url(r'^(?P<project_id>\d+)/$' , views.detail_gallery, name = 'detail_gallery'),
	#url(r'^prices/' , include('prices.urls')),
    #url(r'^recovery/' , include('recovery_info.urls')),

]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
