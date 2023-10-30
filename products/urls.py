from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, RatingViewSet, CommentViewSet, ProductRatingView

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="product")
router.register("ratings", RatingViewSet, basename="rating")
router.register("comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path("product-rating/", ProductRatingView.as_view(), name="product-rating"),
    ]