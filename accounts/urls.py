from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup,name='signup'),
    # path('login/', views.login,name='login'),
    path('login/',views.LoginAPI.as_view(),name='login'),
    path('<str:username>/', views.ProfileAPIView.as_view(),name='profile'),
]