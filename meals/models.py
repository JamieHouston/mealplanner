from django.db import models


class ValueModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Ingredient(ValueModel):
    pass


class Recipe(ValueModel):
    ingredients = models.ManyToManyField(Ingredient)
    cook_time = models.PositiveIntegerField()


class MealDay(models.Model):
    recipe = models.ForeignKey(Recipe)
    day = models.DateField()
