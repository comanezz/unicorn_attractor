from django.conf.urls import url
from .views import all_bugs, create_or_edit_bug, bug_detail, upvote_bug

urlpatterns = [
    url(r'^$', all_bugs, name='all_bugs'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^upvote_bug/$', upvote_bug, name="upvote_bug"),
]
