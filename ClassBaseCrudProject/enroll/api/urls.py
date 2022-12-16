from enroll.api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserView, basename='user_data')

urlpatterns = [
    path('',include(router.urls)),
    

]