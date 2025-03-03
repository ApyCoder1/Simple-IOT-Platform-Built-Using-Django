from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('led-control/', views.led_control, name='led_control'),
    path('led-status/', views.get_led_status, name='get_led_status'),
    path('add-device/',views.add_device, name='add_device'),
    path('device-list/',views.device_list, name='device_list'),
    path('devices/<int:device_id>/control/',views.led_control, name='led_control'),
    path('delete-device/<int:device_id>/', views.delete_device, name='delete_device'),  # URL for deleting a device
    path('devices/toggle/<int:device_id>/', views.toggle_device_activation, name='toggle_device_activation'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]
