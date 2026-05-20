from django.db import models


class World(models.Model):

    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tile(models.Model):

    class Terrain(models.TextChoices):
        GRASS = "grass", "Grass"
        MOUNTAIN = "mountain", "Mountain"
        DESERT = "desert", "Desert"

    world = models.ForeignKey(World, on_delete=models.CASCADE)

    x = models.IntegerField()
    y = models.IntegerField()

    terrain = models.CharField(
        max_length=20, choices=Terrain.choices, default=Terrain.GRASS
    )

    class Meta:
        unique_together = ("world", "x", "y")
        indexes = [
            models.Index(fields=["world", "x", "y"]),
        ]
