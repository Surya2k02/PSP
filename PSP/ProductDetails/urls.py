
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('PSP', views.display, name='PSP'),  # ✅ Fix here
    path('Addproducts/', views.Addproducts),
    path('Addproducts/insertProduct/', views.insertproduct, name='insertProduct'),
    path('editProduct/<int:id>', views.editProducts),
    path('updateProduct/<int:id>', views.updateProducts),
    path('DeleteProduct/<int:id>', views.DeleteProduct),
]