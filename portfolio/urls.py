from django.urls import path
from . import views

app_name='portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:port_id>/', views.detail, name='detail'),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('search/', views.search, name="search"),
    path('<int:port_id>/edit', views.edit, name='edit'),
    path('<int:port_id>/update', views.update, name='update'),
    path('<int:port_id>/delete', views.delete, name="delete"),
]
