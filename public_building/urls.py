from django.conf.urls import url, include
#from django.conf.urls.defaults import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'public_building'
urlpatterns = [
    url(r'^$' , views.building, name='building'),
    url(r'^(?P<building_id>\d+)/$' , views.detail_gallery, name = 'detail_gallery'),

]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
