from django.conf.urls import patterns, url

from deedaday import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),  
    url(r'^$facebook/$', views.index_fb, name='index'),  
    url(r'^$vk/$', views.index_vk, name='index'),  
    url(r'^deeds/(?P<deed_id>\d+)/$', views.deed, name='Deed detail'),   
    url(r'^user/$', views.userpage, name='User page'),   
    url(r'^send/$', views.sendADeed, name='Send your deed'),
    )

