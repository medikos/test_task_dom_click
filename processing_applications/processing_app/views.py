from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer




@api_view(['GET', 'POST'])
# @renderer_classes((JSONRenderer,))
def index(request):
    return Response({1:'Hello'})
    
