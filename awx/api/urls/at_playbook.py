from django.conf.urls import include, url

from awx.api.views import (
    AtPlaybookList,
    AtPlaybookDetail,
    #AtPlaybookLaunch,
)

urls = [
    url(r'^$', AtPlaybookList.as_view(), name='at_playbook_list'),
    url(r'^(?P<pk>[0-9]+)/$', AtPlaybookDetail.as_view(), name='at_playbook_detail'),
    #url(r'^(?P<pk>[0-9]+)/launch/$', AtPlaybookLaunch.as_view(), name='at_playbook_launch'),
]

__all__ = ['urls']
