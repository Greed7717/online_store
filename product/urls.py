from django.urls import path

from product.views import category_view, category_detail_view, product_view, product_detail_view, review_view, \
    review_detail_view, review_product_view, CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, \
    ProductDetailAPIView, ReviewListAPIView, ReviewDetailAPIView, ProductReviewListAPIView

# urlpatterns = [
#     path('catigories/', category_view),
#     path('catigories/<int:id>/', category_detail_view),
#     path("product/", product_view),
#     path("product/<int:id>/", product_detail_view),
#     path("review/", review_view),
#     path("review/<int:id>/", review_detail_view),
#     path("review/product/", review_product_view)
#
# ]

urlpatterns = [
    path('products/categories/', CategoryListAPIView.as_view()),
    path('products/categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('products/products/', ProductListAPIView.as_view()),
    path('products/products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('products/reviews/', ReviewListAPIView.as_view()),
    path('products/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('products/products/reviews/', ProductReviewListAPIView.as_view()),
]
