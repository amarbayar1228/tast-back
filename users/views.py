from .import models
from .import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UsersViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models.Users.objects.get(id=id)
            serializer = serialize.UsersSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = models.Users.objects.all()
        serializer = serialize.UsersSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serialize.UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = models.Users.objects.get(id=id)
        serializer = serialize.UsersSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = models.Users.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    