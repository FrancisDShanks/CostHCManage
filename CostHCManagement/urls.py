from django.conf.urls import url

from CostHCManagement.views import head_count_view

app_name = 'CostHCManagement'
urlpatterns = [
    url(r'^index/$', head_count_view.index, name='index'),
    url(r'^test/$', head_count_view.test, name='test'),
]