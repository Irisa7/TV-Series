from django.conf.urls import url
from .views import search, TVShowPage, Save_like, Season_Page, Episode_Page, Actor_Page, Afficher_series_liked

app_name = 'LikeSeries'
urlpatterns = [
    # ex: /LikeSeries/
    url(r'^$', search, name = 'index'),
    url(r'^TVShow_page/(?P<tv_id>\d+)/$', TVShowPage, name='TVShow_page'),
    url(r'^TVShow_page/$', Save_like, name ='TVShowPage'),
    url(r'^TVShow_page/Bibliothèque$', Afficher_series_liked, name ='Bibliothèque'),
    url(r'^TVShow_page/(?P<tv_id>\d+)/(?P<season_number>\d+)/$', Season_Page, name='Season_Page'),
    url(r'^TVShow_page/(?P<tv_id>\d+)/(?P<season_number>\d+)/(?P<episode_number>\d+)/$', Episode_Page, name='Episode_Page'),
    url(r'^Actor_page/(?P<act_id>\d+)/$',Actor_Page, name ='Actor_Page')
]