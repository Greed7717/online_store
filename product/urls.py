from django.urls import path

from product.views import category_view, category_detail_view, product_view, product_detail_view, review_view, \
    review_detail_view, review_product_view

urlpatterns = [
    path('catigories/', category_view),
    path('catigories/<int:id>/', category_detail_view),
    path("product/", product_view),
    path("product/<int:id>/", product_detail_view),
    path("review/", review_view),
    path("review/<int:id>/", review_detail_view),
    path("review/product/", review_product_view)

]
