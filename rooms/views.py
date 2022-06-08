from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render
from django.http import Http404
from django_countries import countries
from . import models

# Create your views here.
class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


def search(request):

    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)

    room_types = models.RoomType.objects.all()

    return render(
        request,
        "rooms/search.html",
        {
            "city": city,
            "countries": countries,
            "room_types": room_types,
        },
    )


class EditRoomView(UpdateView):

    model = models.Room
    template_name = "rooms/room_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )
