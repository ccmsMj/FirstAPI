from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefualtRouter()
router.register('vehicls', views.vehiclsviewset)

urlpatters = [
    path('', include(router.urls)),
    path('api-auth', include('rest_frameowrk.urls', namespace='rest_framework'))
    
]
