from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from home import views
admin.site.site_header = "first project Admin"
admin.site.site_title = "first project Admin Portal"
admin.site.index_title = "Welcome to my first project content "

urlpatterns = [
    path('',views.about ,name='about'),
    path('index',views.result ,name='result'),
    path('services',views.services ,name='services')
    # path('result',views.result , name='result')
    
]