# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^about$', views.about, name='about'),
#     url(r'^contact$', views.contact, name='contact'),
# ]
from django.urls import path  # Correct import for Django 4.x
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
