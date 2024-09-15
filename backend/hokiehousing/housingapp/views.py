from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import UserPreferences


@csrf_exempt
def submit_quiz(request):
    try:
        data = json.loads(request.body)
        
        preferences = UserPreferences.objects.create(
            desired_price = data["desired_price"],
            utilities = data["utilities_included"],
            bedrooms = data['desired_bedrooms'],
            bathrooms = data["desired_bathrooms"],
            amenities = data['desired_amenities'],
            public_transit = data['public_transport']
        )

        return JsonResponse({'status': 'success', 'user_token': preferences.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def get_apartment_listings(request):

    
    pass

def calculate_score(apartment, preferences):
    importance = preferences.importance


    pass

def get_apartment_details(request, apartment_id):
    pass

