from django.conf.urls import patterns, url, include
from rest_framework import routers
from account import views
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^client/' , include('clientmodels.urls')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
)






# from django.conf.urls import patterns, include, url
# 



# # from account.api import *
# 


# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'flatPI.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^ac/', include(account.urls)),
#     url(r'^admin/', include(admin.site.urls)),
# )
