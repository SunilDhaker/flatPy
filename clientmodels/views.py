from .models import Venders , Bill
from .serializers import VenderSerializer , BillSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class VenderList(APIView):
    """
    List all Venders, or create a new Vender.
    """
    def get(self, request, format=None):
        vender = Venders.objects.all()
        serializer = VenderSerializer(vender, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VenderSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VenderDetail(APIView):
    """
    Retrieve, update or delete a Vender instance.
    """
    def get_object(self, pk):
        try:
            return Venders.objects.get(pk=pk)
        except Venders.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Vender = self.get_object(pk)
        serializer = VenderSerializer(Vender)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Vender = self.get_object(pk)
        serializer = VenderSerializer(Vender, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Vender = self.get_object(pk)
        Vender.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class BillList(APIView):
	def get(self , request , format=None):
		bills = Bill.objects.all()
		serializer = BillSerializer(bills, many=True)
		return Response(serializer.data)