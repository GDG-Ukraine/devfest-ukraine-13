from django.conf.urls.defaults import url, patterns, include
#from django.contrib import admin
#admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns(
    '',
    url(r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    #(r'^adminenter/', include(admin.site.urls)),

    url(r'^$', 'app.views.index', name='index'),
    url(r'^agenda/$', 'app.views.agenda', name='agenda'),
    url(r'^location/$', 'app.views.location', name='location'),
    url(r'^speakers/$', 'app.views.speakers', name='speakers'),
    url(r'^photos/$', 'app.views.photos', name='photos'),
)
