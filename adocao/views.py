from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import AdocaoSerializer


class AdocaoList(APIView):
    def post(seçf, request, format=None):
        serializer = AdocaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houveram erros de validação!",
            },
            status=HTTP_400_BAD_REQUEST
        )
