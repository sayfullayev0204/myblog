from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def code(request):
    return render(request, 'code.html')
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserLocation
@csrf_exempt  # Test uchun. Agar CSRF muammosi bo'lmasa, bu qatorni olib tashlang
def save_location(request):
    if request.method == "POST":
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        
        # IP manzilni olish
        ip_address = request.META.get("REMOTE_ADDR", "")

        # Ma'lumotni bazaga saqlash
        UserLocation.objects.create(
            ip_address=ip_address,
            latitude=latitude,
            longitude=longitude
        )

        return JsonResponse({"status": "success", "message": "Joylashuv saqlandi!"})

    return JsonResponse({"error": "Yaroqsiz so'rov"}, status=400)