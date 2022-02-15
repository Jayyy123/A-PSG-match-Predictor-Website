from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from predictorapi.serializers import PredictorS


links = {
    'database':'/predictorapi/database/',
    'create':'/predictorapi/create/',
    'delete': '/predictorapi/delete/',
}


@api_view(['GET'])
def listLinks(request):
    list = links
    return Response(list)

@api_view(['POST'])
def database(request):
    a = PredictorS()
    return Response(a)

@api_view(['GET'])
def createPrediction(request):
    a = PredictorS()
    return Response(a)

@api_view(['POST'])
def delete(request):
    a = PredictorS()
    return Response(a)


