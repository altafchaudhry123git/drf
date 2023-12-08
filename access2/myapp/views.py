from django.shortcuts import render, HttpResponse
import requests
from rest_framework.decorators import api_view
from .models import *

from django.http import JsonResponse

@api_view(['POST','GET'])
def api_example_view(request):
    api_url='http://127.0.0.1:9000/csv_upload_api'
    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNTg5MTU2LCJpYXQiOjE3MDE1ODg4NTYsImp0aSI6IjU2MTljYWMxNzExNDRiZGZiN2RmOTRkNGMzYTBlMzVmIiwidXNlcl9pZCI6MX0.LFmNSDZIA_OhnLo7cg2ZNUVpLD_xU0S-hl0mXuZS3HY"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        print('workingggg')
        api_data = response.json()
        k=len(api_data["data"])
        for i in range(k):
            print(api_data["data"][i]['name'])
            Student.objects.create(
                    name=api_data["data"][i]['name'],
                    gender=api_data["data"][i]['gender'],
                    department=api_data["data"][i]['department'],
                    dob=api_data["data"][i]['dob'],
                    city=api_data["data"][i]['city']
                    )                 
            k=k+1        
        return JsonResponse(api_data)
    else:
        # Handle the error
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=500)

    