from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Game(models.Model):
    category = models.ManyToManyField(Category)
    name=models.CharField(max_length=255)
    information=models.TextField(null=True)
    price=models.IntegerField(null=True)
    price_off=models.IntegerField(null=True)
    image=models.ImageField(upload_to='img/',null=True)
    status=models.BooleanField(default=False)




