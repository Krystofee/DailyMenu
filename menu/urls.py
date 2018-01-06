from django.conf.urls import url

from menu.views.menu import MenuListView, MenuUpdateView, MenuCreateView, MenuDeleteView

app_name = 'menu'
urlpatterns = [
    url(r'^$', MenuListView.as_view(), name='list'),
    url(r'^create/$', MenuCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9a-f-]+)/$', MenuListView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[0-9a-f-]+)/$', MenuUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9a-f-]+)/$', MenuDeleteView.as_view(), name='delete'),
]
