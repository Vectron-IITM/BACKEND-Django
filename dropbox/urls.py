from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('dropBox', views.DropBoxView)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('register', views.register, name='register')
]