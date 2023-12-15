from django.contrib import admin
from django.urls import path, include

from product.views import category_view, category_detail_view
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("product.urls")),
    path('users/registration/', views.registration_api_view),
    path('users/confirm/', views.confirm_user_api_view),
    path('users/authorization/', views.authorization_api_view)

]
# {
# "username":"Happy",
# "password":"12345678"
# }