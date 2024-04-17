from django.db import models

class Game(models.Model):
    name=models.CharField(max_length=255)
    information=models.TextField(null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='img/',null=True)

    def __str__(self):
        return self.name
