from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name



class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    value = models.IntegerField(choices=[(1, "Poor"), (2, "Fair"), (3, "Good"), (4, "Very good"), (5, "Excellent")])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} for {self.product}"

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} commented on {self.product}"