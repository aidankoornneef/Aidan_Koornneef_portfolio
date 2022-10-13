from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name='homeview'),
    path('projects/',views.projects,name='projectview'),
    path('work/',views.work,name='workview'),
]

urlpatterns += staticfiles_urlpatterns()