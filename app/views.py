from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def code(request):
    return render(request, 'code.html')
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def save_location(request):
    if request.method == "POST":
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        print(latitude, longitude)
        return JsonResponse({"message": "Joylashuv saqlandi", "latitude": latitude, "longitude": longitude})
