from django.db.models import Avg
from rest_framework import serializers
from .models import Product, Rating, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price"]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "product", "value", "created"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "product", "text", "author", "created"]


class ProductRatingSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


    def validate_product_id(self, value):
        try:
            product = Product.objects.get(id=value)

        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with this id does not exist")
        return value

    def to_representation(self, instance):

        product = Product.objects.get(id=instance.validated_data["product_id"])

        average_rating = Rating.objects.filter(product=product).aggregate(Avg("value"))["value__avg"]
        comments = Comment.objects.filter(product=product)
        ratings_data = RatingSerializer(product.ratings, many=True).data
        comments_data = CommentSerializer(comments, many=True).data

        return {
            "product": product.name,
            "average_rating": average_rating,
            "ratings": ratings_data,
            "comments": comments_data
        }