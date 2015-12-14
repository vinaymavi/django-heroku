from django.conf.urls import url
from . import views
# TODO what is name argument.
urlpatterns = [
    url(r'^$', views.index, name="index")
]
