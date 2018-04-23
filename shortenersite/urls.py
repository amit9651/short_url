from django.conf.urls import *

urlpatterns = patterns('shortenersite.views',
    url(r'^$', 'index', name='home'),
    url(r'^(?P&1t;short_id&gt; \w{6})$','redirect_original',name='redirectoriginal'),
    url(r'^makeshort/$', 'shorten_url',name='shortenurl'),
    )
