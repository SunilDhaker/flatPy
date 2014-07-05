from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Venders , Bill


@api_view(['POST' , 'GET'])
def venders(request):
    message = 'No error'
    status = 0
    objectsArray = []
    data = request.DATA
    

    if request.method == 'POST':
        data = request.DATA
        for entry in data['objectsArray'] :
            try:
                addVender(brand = entry['brand'] ,place =  entry['place'] ,imagepath =  entry['image'])
            except:
                pass
    


    if request.method == 'GET':
        for vender in Venders.objects.all():
            objectsArray.append({'brand': vender.brand , 'place' : vender.place , 'image':vender.image.path })
    responce_object = {"status": {'status':status , 'message':message} , 'objectsArray' : objectsArray  }
    
    return Response(responce_object)


def addVender(brand , place , imagepath):
    vender = Venders()
    vender.brand = brand
    vender.place = place
    # vender.image = None
    vender.save()