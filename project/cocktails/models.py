import os
from urllib.request import urlretrieve

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models


class Glass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Measure(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    alcoholic = models.BooleanField()
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    glass = models.ForeignKey(Glass, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    ingredient1 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient1_set", blank=True, null=True)
    ingredient2 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient2_set", blank=True, null=True)
    ingredient3 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient3_set", blank=True, null=True)
    ingredient4 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient4_set", blank=True, null=True)
    ingredient5 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient5_set", blank=True, null=True)
    ingredient6 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient6_set", blank=True, null=True)
    ingredient7 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient7_set", blank=True, null=True)
    ingredient8 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient8_set", blank=True, null=True)
    ingredient9 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient9_set", blank=True, null=True)
    ingredient10 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient10_set", blank=True, null=True)
    ingredient11 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient11_set", blank=True, null=True)
    ingredient12 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient12_set", blank=True, null=True)
    ingredient13 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient13_set", blank=True, null=True)
    ingredient14 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient14_set", blank=True, null=True)
    ingredient15 = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient15_set", blank=True, null=True)
    measure1 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure1_set", blank=True, null=True)
    measure2 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure2_set", blank=True, null=True)
    measure3 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure3_set", blank=True, null=True)
    measure4 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure4_set", blank=True, null=True)
    measure5 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure5_set", blank=True, null=True)
    measure6 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure6_set", blank=True, null=True)
    measure7 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure7_set", blank=True, null=True)
    measure8 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure8_set", blank=True, null=True)
    measure9 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure9_set", blank=True, null=True)
    measure10 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure10_set", blank=True, null=True)
    measure11 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure11_set", blank=True, null=True)
    measure12 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure12_set", blank=True, null=True)
    measure13 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure13_set", blank=True, null=True)
    measure14 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure14_set", blank=True, null=True)
    measure15 = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name="measure15_set", blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    def get_image(self, url):
        """Fetch an image file via URL and save it to self.image"""
        result = urlretrieve(url)
        self.image.save(
            name=os.path.basename(url),
            content=File(open(result[0], 'rb')),
        )
