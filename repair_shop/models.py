from django.db import models


# Create your models here.
class Repair(models.Model):
    code = models.CharField(max_length=10, unique=True)
    date = models.DateField(auto_now=True)
    description = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    repair_shop = models.ForeignKey('RepairShop', on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Car(models.Model):
    type_select = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
    ]
    color_select = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Silver', 'Silver'),
    ]
    type = models.CharField(max_length=255, choices=type_select)
    brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=255, choices=color_select)

    def __str__(self):
        return f'{self.brand} {self.type} {self.color}'


class RepairShop(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    repairsOldTimers = models.BooleanField()

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=255)
    site_link = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RepairShopRepairsCarBrand(models.Model):
    repair_shop = models.ForeignKey('RepairShop', on_delete=models.CASCADE)
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.repair_shop} {self.car_brand}'
