from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^post/(?P<image_id>[0-9]+)/review_engine/$', views.rate_engine, name='rate_engine'),
    url(r'^post/(?P<image_id>[0-9]+)/review_usability/$', views.rate_usability, name='rate_usability'),
    url(r'^post/(?P<image_id>[0-9]+)/review_body/$', views.rate_body, name='rate_body'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^upload_image/$', views.upload_image, name='upload_image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^profile/update/$', views.edit_profile, name='edit_profile'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)