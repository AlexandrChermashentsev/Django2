from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name='index'),
    path("orders/<int:client_id>/", views.customer_orders, name='orders'),
    path('client/<int:client_id>/', views.show_client, name='show_client'),
    path('clent_form/', views.client_form, name='client_form'),
    path('product_form/', views.product_form, name='product_form'),
    # path('media/media/<str:img>/', views.img_view, name='img_view'),

]