from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='about/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Branches(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    img = models.ImageField(upload_to='branches/', null=True, blank=True)

    def __str__(self):
        return self.name


class Requirements(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    requirements = models.ManyToManyField(Requirements, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def get_meal(self):
        return Meal.objects.filter(category=self)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id.username


class Meal(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='foods/')
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_total_price(self):
        return self.price * Basket.objects.get(meal=self).quantity

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_price(self):
        return self.meal.price * self.quantity

    def __str__(self):
        return self.order.user_id.username


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.meal.name

