from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_openapi.utils import view_config
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    @view_config(response_serializer=SnippetSerializer)
    def get(self, request, version, format=None):
        snippets = Snippet.objects.all()
        res = self.response_serializer(snippets, many=True)
        res .is_valid(raise_exception=True)
        return Response(res.validated_data)

    @view_config(request_serializer=SnippetSerializer, response_serializer=SnippetSerializer)
    def post(self, request, version, format=None):
        req = self.request_serializer(data=request.data)
        req.is_valid(raise_exception=True):
        req.save()
        res = self.response_serializer(req.data)
        res .is_valid(raise_exception=True)
        return Response(res.validated_data, status=status.HTTP_201_CREATED)