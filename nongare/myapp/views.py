from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contact': reverse('contact-list', request=request, format=format),

    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer