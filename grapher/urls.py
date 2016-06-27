from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import grapher.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', grapher.views.index, name='index'),
    # url(r'^db', grapher.views.db, name='db'),
    url(r'^graph/(?P<graph_title>\w{0,256})/$', grapher.views.generateGraphView, name='generateGraphView'),
    url(r'^admin/', include(admin.site.urls)),

]
