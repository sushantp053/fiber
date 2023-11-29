from django.shortcuts import render
from home.models import *
from django.core.serializers import serialize
from django.db.models import Count

# Create your views here.


def home(request):
    markerList = list(Marker.objects.all().values())
    d = serialize("geojson", Talav.objects.all())
    data = {"data": d}
    context = {"markers": markerList, "talav": data}

    return render(request, "index.html", context)


def natoshiData(request):
    markerList = list(Marker.objects.all().values())
    d = serialize("geojson", Natoshi.objects.all())
    data = {"data": d}
    distinct_crop = Natoshi.objects.distinct("crop").all()

    total_count = Natoshi.objects.distinct().count()
    count_crop = Natoshi.objects.all().values("crop").annotate(
        count=Count('crop', distinct=False))
    # crops = {"crop": distinct_crop}
    # print(crops)
    context = {"markers": markerList, "talav": data,
               "crop": distinct_crop, "crop_count": count_crop, "total": total_count}

    return render(request, "natoshi.html", context)


def addMarker(request):
    data = request.POST
    if (request.method == "POST"):
        name = data["name"]
        addr = data["addr"]
        lat = data["lat"]
        lng = data["lng"]

        Marker.objects.create(name=name, addr=addr, lng=lng, lat=lat)

    return render(request, "add.html")
