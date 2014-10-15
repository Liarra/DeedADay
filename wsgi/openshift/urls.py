from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'deedaday.views.index', name='index'),  
    url(r'^deeds/(?P<deed_id>\d+)/$',  'deedaday.views.deed', name='Deed detail'),   
    url(r'^user/(?P<user_id>\d+)/$',  'deedaday.views.userpage', name='User page'),   
    url(r'^send/$',  'deedaday.views.sendADeed', name='Send your deed'),
)
