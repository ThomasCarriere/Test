from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Accueil, name='Accueil'),
    url(r'^(?P<TicketIncident_id>[0-9]+)/$', views.Detail, name='Detail'),
    url(r'^Ajout/$', views.Ajout, name='Ajout'),
    url(r'^Ajouter/$', views.Ajouter, name='Ajouter'),]

