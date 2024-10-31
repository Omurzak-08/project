from django.db import models


class Marka(models.Model):
    marka_name = models.CharField(max_length=16, unique=True)



    def __str__(self):
        return self.marka_name


class Model(models.Model):
    model_name = models.CharField(max_length=16, null=True, blank=True)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE,related_name='model')


    def __str__(self):
        return self.model_name


class Car(models.Model):
    title_name = models.CharField(max_length=32)
    description = models.TextField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=10)
    volume = models.PositiveSmallIntegerField(default=0)
    year = models.IntegerField()
    type_change = models.BooleanField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    video = models.FileField(upload_to='vid/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title_name}'