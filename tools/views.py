from django.shortcuts import render, get_object_or_404
from world.models import World, Tile


def world_view(request, world_id):
    world = get_object_or_404(World, id=world_id)

    center_x = int(request.GET.get("x", 0))
    center_y = int(request.GET.get("y", 0))
    radius = int(request.GET.get("r", 10))

    tiles = Tile.objects.filter(
        world=world,
        x__gte=center_x - radius,
        x__lte=center_x + radius,
        y__gte=center_y - radius,
        y__lte=center_y + radius,
    )

    tile_map = {(t.x, t.y): t for t in tiles}

    grid = []
    for y in range(center_y - radius, center_y + radius + 1):
        row = []
        for x in range(center_x - radius, center_x + radius + 1):
            row.append(tile_map.get((x, y)))
        grid.append(row)

    diameter = radius * 2 + 1

    return render(
        request,
        "world_view.html",
        {
            "world": world,
            "grid": grid,
            "center_x": center_x,
            "center_y": center_y,
            "radius": radius,
            "diameter": diameter,
        },
    )
