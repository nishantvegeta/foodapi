from django.shortcuts import render, redirect
from .models import Food
from .serializers import FoodSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def food_list(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def food_detail(request, id):
    try:
        food = Food.objects.get(pk=id)
    except food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FoodSerializer(food)
    return Response(serializer.data)

@api_view(['POST'])
def food_post(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_food(request, id):
    try:
        food = Food.objects.get(pk = id)
    except food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FoodSerializer(food, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)