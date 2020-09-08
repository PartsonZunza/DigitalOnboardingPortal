from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('update_product/', views.update_product, name="update_product"),
    path('product_view/<str:id>/', views.product_view, name="product_view"),
    path('products/', views.products_view, name='products'),
    path('product_add/', views.product_add, name='product_add'),
    path('find/', views.find, name='find'),
    path('reports/', views.reports, name='reports'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)