from django.db import models


class Pet(models.Model):
    TYPE_CHOICES = (
        ("dog", "Dog"),
        ("cat", "Cat"),
        ("parrot", "Parrot"),
        ("koala", "Koala"),
    )
    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)