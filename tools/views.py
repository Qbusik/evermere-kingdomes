from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect

from tools.forms import RegisterForm
from world.models import World, Tile


def tools_home(request):
    worlds = World.objects.all().order_by("id")

    return render(request, "tools_home.html", {"worlds": worlds})


def register_user_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/tools/")

    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


def world_view(request, world_id):
    world = get_object_or_404(World, id=world_id)

    center_x = int(request.GET.get("x", 10))
    center_y = int(request.GET.get("y", 10))
    radius = int(request.GET.get("r", 8))
    radius = max(1, min(radius, 8))

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
