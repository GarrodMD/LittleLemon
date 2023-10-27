#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
   path('', views.index, name='home'),
   path('about/', views.about, name="about"),
   path('menu/', views.MenuItemView.as_view(), name='menu'),
   path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-items'),
   path('reservations/', views.reservations, name="reservations"),
   path('booking/', include(router.urls)),

]