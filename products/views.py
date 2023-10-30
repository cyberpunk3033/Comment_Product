from rest_framework import viewsets
from .models import Product, Rating, Comment
from .serializers import ProductSerializer, RatingSerializer, CommentSerializer, ProductRatingSerializer

from rest_framework.response import Response
from rest_framework import generics

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class ProductRatingView(generics.GenericAPIView):
    serializer_class = ProductRatingSerializer

    def get(self, request):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.to_representation(serializer)
        return Response(data)
