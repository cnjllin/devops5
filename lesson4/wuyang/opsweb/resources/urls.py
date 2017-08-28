from django.conf.urls import include, url

from . import idc

urlpatterns = [
    url(r'idc/', include([
        url(r'add/$', idc.CreateIdcView.as_view(), name="idc_add"),
    ]))
]
