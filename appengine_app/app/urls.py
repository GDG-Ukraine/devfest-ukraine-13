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
    url(r'^team/$', 'app.views.team', name='team'),
    url(r'^devfest2012/$', 'app.views.devfest2012', name='devfest2012'),
    url(r'^summit/$', 'app.views.summit', name='summit'),
    url(r'^hackathon/$', 'app.views.hackathon', name='hackathon'),
    url(r'^conference/$', 'app.views.conference', name='conference'),
    url(r'^registration/$', 'app.views.registration', name='registration'),
)
