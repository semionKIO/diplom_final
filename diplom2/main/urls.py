from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name = 'home'),
    # path('worker', views.worker),
    path('reviews', views.reviews,name = 'reviews'),
    path('rate', views.rate, name = 'rate'),
    path('contact', views.contact, name='contact'),
    path('documents', views.documents, name='documents'),


]
