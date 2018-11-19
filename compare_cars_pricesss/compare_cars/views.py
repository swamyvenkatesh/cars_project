from .models import Car_Master_Data,CarDetails
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import CompareCarSerializer,MaterCarSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response







# master data views

class Get_allMakes(generics.ListCreateAPIView):
    """
    List all boards, or create a new board.
    """
    # queryset_results = CarMakeDetails.objects.order_by().values('makes').distinct()
    print "car_make"
    queryset = CarDetails.objects.order_by("price").filter(city="Delhi")
    # print queryset
    serializer_class = CompareCarSerializer




# scrapped  data views
@api_view(['GET'])
def Get_allMakesDetails(request,car_make):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        models= CarDetails.objects.filter(car_make=car_make)
        #print models
    except models.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompareCarSerializer(models,many=True)
        lookup_field = 'car_make'
        return Response(serializer.data)

# class Get_allMakesDetails(views.APIView):
#     queryset = CarMakeDetails.objects.filter(makes='Tata')
#     serializer_class = CompareCarSerializer

@api_view(['GET'])
def Get_allModelDetails(request,car_make,car_model):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        print "models"
        makes_set = CarDetails.objects.order_by("price").filter(car_make=car_make)
        models_set = makes_set.filter(car_model=car_model)
        # for model in models_set:
        #     print '*********************'
        #     print model.car_image
    except:
        # return Response(status=status.HTTP_404_NOT_FOUND)
        print "error"

    if request.method == 'GET':
        serializer = CompareCarSerializer(models_set,many=True)
        lookup_field = 'car_make'
        s_data = serializer.data
        for s in s_data:
            print s["car_image"]
        # print "-----------------------------------------------"
        # print serializer.data
        # print "-----------------------------------------------"
        return Response(serializer.data)


@api_view(['GET'])
def Get_DataFromCity(request,city):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        print "cities"
        city_search =city.title()
        city_data = CarDetails.objects.order_by("price").filter(city=city_search)
        # city_data = CarDetails.objects.order_by("price").filter(city=city)
        print city_data
    except city_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompareCarSerializer(city_data,many=True)
        lookup_field = 'car_make'
        print "-----------------------------------------------"
        print serializer.data
        print "-----------------------------------------------"
        return Response(serializer.data)


@api_view(['GET'])
def Get_AllDataFromCity(request,city,car_make,car_model):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        print "cities"
        city_search =city.title()
        makes = CarDetails.objects.order_by("price").filter(city=city_search)
        models = makes.filter(car_make=car_make)
        models_set = models.filter(car_model=car_model)
        
    except models_set.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompareCarSerializer(models_set,many=True)
        lookup_field = 'car_make'
        print "-----------------------------------------------"
        print serializer.data
        print "-----------------------------------------------"
        return Response(serializer.data)


