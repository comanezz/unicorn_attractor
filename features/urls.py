from django.conf.urls import url
from .views import all_features

urlpatterns = [
    url(r'^$', all_features, name='all_features'),
]