from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from clientmodels import views

urlpatterns = patterns('',
    url(r'^venders/$', views.venders),
    # url(r'^venders/(?P<pk>[0-9]+)/$', views.VenderDetail.as_view()),
    # url(r'^bills/$' , views.BillList.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)