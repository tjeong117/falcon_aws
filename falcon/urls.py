from django.urls import path

from . import views

urlpatterns = [

    path('', views.index),
    path('main', views.main),
    path('common/top', views.top),
    path('projects/datascience/stock/stock', views.stock),
    path('projects/datascience/stock/stock_demo', views.stock_demo),
    path('projects/datascience/stock/stock_graph', views.stock_graph),
    path("introduce/introduction", views.introduction),
    path('projects/computation/computation_science', views.computational_science),
    path('award/award', views.award),
    path('resume/resume', views.resume)
]



