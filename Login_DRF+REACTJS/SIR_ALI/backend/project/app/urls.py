from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('password/reset/', views.password_reset, name='password_reset'),
    path('password/update/', views.password_update, name='password_update'),
]
