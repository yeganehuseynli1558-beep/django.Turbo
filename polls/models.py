from django.db import models

class CarAd(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField()
    image = models.ImageField(upload_to='car_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} - {self.price} AZN"
