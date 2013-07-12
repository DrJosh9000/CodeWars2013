from django.conf.urls.defaults import *

urlpatterns = patterns('PRISM.codewars.views',
	(r'^$', 'index'),
	(r'^chemtrails/$', 'chemtrails'),
	(r'^time/$', 'time'),
	(r'^backdoor/$', 'backdoor'),
	(r'^illuminati/$', 'illuminati'),
	(r'^leaderboard/$', 'leaderboard'),
	(r'^credits/$', 'credits')
)

