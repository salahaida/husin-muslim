from django.conf.urls import url
from . import views

my_app="Content Arabic"

urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^(?P<id>\d+)$', views.post, name='post'),

    url(r'^about$', views.about, name='about'),
    url(r'^connect$', views.connect, name='connect'),

]
