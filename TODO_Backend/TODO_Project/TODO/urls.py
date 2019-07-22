from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTODO.as_view()),
    path('<int:pk>', views.DetailsTODO.as_view()),
]
