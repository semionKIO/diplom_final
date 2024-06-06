from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import WeDetailView

urlpatterns = [
    path('', views.index_we,name = 'home_we'),
    path('workers', views.workers, name='workers'),
    path('<int:pk>', views.WeDetailView.as_view(), name='we_detail'),
    path('workers/<int:pk>', views.WorkDetailView.as_view(), name='work_detail'),

]
urlpatterns += staticfiles_urlpatterns()


