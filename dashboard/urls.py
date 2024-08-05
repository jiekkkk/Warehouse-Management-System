from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/view/<int:pk>/', views.staff_view, name='dashboard-staff-view'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='dashboard-staff-delete'),
    path('product/', views.product, name='dashboard-product'),
    path('product/status/', views.product_status, name='dashboard-product-status'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),
    path('order/delete/<int:pk>/', views.order_delete, name='dashboard-order-delete'),
    path('order/update/<int:pk>/', views.order_update, name='dashboard-order-update'),

]