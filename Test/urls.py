from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


router = routers.DefaultRouter()
router.register('user', views.Users)
router.register('order', views.Orders)
router.register('product', views.Products)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.Index.as_view()),
    path('users/create/', views.CreateUser.as_view()),
    path('product/create/', views.CreateProduct.as_view()),
    path('order/create/', views.CreateOrder.as_view()),
    #path('order/', views.Orders.as_view()),
    #path('product/', views.Products.as_view()),
    #path('users/', views.Users.as_view()),
]