from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [

    re_path(r'^student/info/$', Student_list, name='Student-list'),
    re_path(r'^student/info/(?P<pk>\d+)/$', Student_list, name='Student-detail'),
    re_path(r'^student/info/filter/$', Student_filter, name='Student-filter'),
    re_path(r'^student/info/delete/(?P<pk>\d+)/$', Student_delete, name='Student-delete'),
    
    re_path(r'^/savefile/', SaveFile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)