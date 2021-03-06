from django.urls import path
from usermgmt import views

urlpatterns = [
    path('', views.list_music, name = 'list_music'),
    path('new/', views.create_music, name = 'add_music'),
    path('update/<int:id>/', views.update_music, name = 'update_music'),
    path('delete/<int:id>/', views.delete_music, name = 'delete_music'),
]
