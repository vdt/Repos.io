# Repos.io / Copyright Stephane Angel / Creative Commons BY-NC-SA license

from django.conf.urls.defaults import *
from search.views import RepositorySearchView, AccountSearchView


urlpatterns = patterns('',
    url(r'^$', RepositorySearchView(), name='search'),
    url(r'^users/$', AccountSearchView(), name='search_accounts'),
)
