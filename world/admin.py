import random

from django.contrib import admin

from world.models import World, Tile


@admin.action(description="Generate world tiles")
def generate_world_tiles(modeladmin, request, queryset):
    for world in queryset:
        tiles = []

        for x in range(world.width):
            for y in range(world.height):

                tiles.append(
                    Tile(
                        world=world,
                        x=x,
                        y=y,
                        terrain=random.choices(
                            population=[
                                Tile.Terrain.GRASS,
                                Tile.Terrain.MOUNTAIN,
                                Tile.Terrain.DESERT,
                            ],
                            weights=[80, 10, 10],
                            k=1,
                        )[0],
                    )
                )

        Tile.objects.bulk_create(tiles, ignore_conflicts=False)
        modeladmin.message_user(request, "World generated!")


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    actions = [generate_world_tiles]
    list_display = ("id", "name", "width", "height", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ("id", "world", "x", "y", "terrain")
    list_filter = ("terrain", "world")
    search_fields = ("world__name",)
    ordering = ("world", "x", "y")
