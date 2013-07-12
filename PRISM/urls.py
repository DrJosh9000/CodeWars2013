from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    ('handler404', 'django.views.defaults.page_not_found'),
#    ('handler500', 'django.views.defaults.server_error'),

    # Example:
    # (r'^PRISM/', include('PRISM.foo.urls')),
    (r'^', include('PRISM.codewars.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
