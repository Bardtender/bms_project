from django.conf.urls import url

from . import views

# list the view (controller) to be used to render each template
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chart_data/$', views.chart_data, name='chart_data')
]