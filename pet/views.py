from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Pet
from .serializers import PetSerializer


class PetList(APIView):
    def get(self, request, format=None):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
