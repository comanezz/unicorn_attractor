from django.conf.urls import url
from .views import all_features, feature_detail

urlpatterns = [
    url(r'^$', all_features, name='all_features'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/$', feature_detail, name='feature_detail'),
]