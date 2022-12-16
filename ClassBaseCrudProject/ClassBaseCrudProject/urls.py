
from django.contrib import admin
from django.urls import path,include
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserDataView.as_view(),name='addnshow'),
    # path('', views.addshow, name='addnshow'),
    path('delete/<int:id>/', views.Delte.as_view(), name='deletedata'),
    path('<int:id>/', views.UpdateOrEdit.as_view(), name='updatedata'),
    path('api/',include('enroll.api.urls')),
    path('login/',include('rest_framework.urls'))
]
