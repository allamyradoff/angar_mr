from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Dukanlar(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ady = models.CharField(max_length=150)
    welayat = models.CharField(max_length=15)
    salgy = models.CharField(max_length=255)
    tel1 = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15)
    geo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'dukanlar'

    def __str__(self):
        return self.ady


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'car'

    def __str__(self):
        return self.name


class Zapcas(models.Model):
    title = models.CharField(max_length=100)
    # Field name made lowercase.
    priceman = models.FloatField(db_column='priceMan')
    notes = models.CharField(max_length=255)
    # Field name made lowercase.
    carids = models.CharField(db_column='carIds', max_length=255)
    # Field name made lowercase.
    catid = models.CharField(db_column='catId', max_length=255)
    yagday = models.IntegerField(default=0)
    tel = models.CharField(max_length=100, default=99363370891)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'zapcas'

    def __str__(self):
        return self.title


class Car_model(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'car_model'

    def __str__(self):
        return self.name


class Cars_category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category_cars'

    def __str__(self):
        return self.name


class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rating'

    def __str__(self):
        return self.name