from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'products-access', ProductAccessViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'lessonView', LessonViewViewSet, basename='lesson-view')

urlpatterns = [
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]