from django.shortcuts import render
from django.http import JsonResponse
from wrest.models import dafare
from wrest.serializers import dafareSerializer
# Create your views here.

def dafare_list(request):
    d = dafare.objects.all()
    s=dafareSerializer(d, many=True)
    return JsonResponse(s.data, safe=False)
    

