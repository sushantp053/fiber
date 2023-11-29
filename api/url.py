from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'natoshi', NatoshiViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
