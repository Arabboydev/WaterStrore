from django.db import models
from django.db.models.functions import datetime

from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator


class CategoryWaters(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_waters'

    def __str__(self):
        return self.name


class Waters(models.Model):
    category = models.ForeignKey(CategoryWaters, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='waters/', default='default_img/water_img.png')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    volume = models.IntegerField()
    about = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'waters'

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.CharField(max_length=255)
    star_given = models.IntegerField(
        default=0,
        validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
        ]
    )
    water = models.ForeignKey(Waters, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"{self.star_given} {self.water.name} {self.user.username}"



