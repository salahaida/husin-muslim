from django.conf.urls import url
from . import views

my_app="Content Arabic"

urlpatterns = [
    url(r'^$', views.all_posts_en, name='all_posts_en'),
    url(r'^(?P<id>\d+)$', views.post_en, name='post_en'),

    url(r'^about_en$', views.about_en, name='about_en'),
    url(r'^connect_en$', views.connect_en, name='connect_en'),


]
