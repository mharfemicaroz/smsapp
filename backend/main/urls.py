from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = []

# Function to add URL patterns for a given model
def add_model_urlpatterns(model):
    model_name = model.__name__
    urlpatterns.extend([
        re_path(rf'^{model_name.lower()}/info/$', globals()[f'{model_name}_list'], name=f'{model_name.lower()}-list'),
        re_path(rf'^{model_name.lower()}/info/(?P<pk>\d+)/$', globals()[f'{model_name}_list'], name=f'{model_name.lower()}-detail'),
        re_path(rf'^{model_name.lower()}/info/filter/$', globals()[f'{model_name}_filter'], name=f'{model_name.lower()}-filter'),
        re_path(rf'^{model_name.lower()}/info/delete/(?P<pk>\d+)/$', globals()[f'{model_name}_delete'], name=f'{model_name.lower()}-delete'),
    ])

# Generate URL patterns for each model
for model in models:
    add_model_urlpatterns(model)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)