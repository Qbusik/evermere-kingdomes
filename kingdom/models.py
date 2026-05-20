from django.db import models

from evermere_kingdomes import settings


class Kingdom(models.Model):

    world = models.ForeignKey(
        "world.World", on_delete=models.CASCADE, related_name="kingdoms"
    )

    name = models.CharField(max_length=20)

    capital_x = models.IntegerField()
    capital_y = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
