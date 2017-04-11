from django.conf.urls import url, include
#from django.conf.urls.defaults import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'design_interera'
urlpatterns = [
    url(r'^$' , views.design_intr, name='design_intr'),
    url(r'^(?P<interer_id>\d+)/$' , views.detail_gallery, name = 'detail_gallery'),

]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)