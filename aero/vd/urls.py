from django.urls import path

from .views import index, VDLogoutView, VDLoginView

app_name = 'vd'

urlpatterns = [
    path('accounts/logout/', VDLogoutView.as_view(), name='logout'),
    path('accounts/login/', VDLoginView.as_view(), name='login'),
    path('', index, name='index'),
]
