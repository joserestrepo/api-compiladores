from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from api.models import Archivos
from api.serializers import ArchivoSerializer
import api.compilador.parser as parser

# Create your views here.

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET'])
def lista_archivos(request):
    archivos = Archivos.objects.all()
    serializer = ArchivoSerializer(archivos, many = True)
    return JSONResponse(serializer.data)

@api_view(['POST'])
def guardarArchivo(request):
    data = JSONParser().parse(request)
    serializer = ArchivoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)    

@api_view(['PUT'])
def actualizarArchivo(request):
    data = JSONParser().parse(request)
    try:
        archivo = Archivos.objects.get(pk=data['id'])
    except:
        return HttpResponse(status=404)
        
    serializer = ArchivoSerializer(archivo, data = data)

    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)   

@api_view(['POST'])
def compilar(request):
    data = JSONParser().parse(request)
    print(data)
    parser.VERBOSE = 0
    try:
        parser.parser.parse(data['text'], tracking=True)
        return JSONResponse({'compilacion':True})
    except:
        return JSONResponse({'compilacion':False})  


@api_view(['DELETE'])
def eliminarArchivo(request,pk):
    try:
        archivo = Archivos.objects.get(pk=pk)
    except:
        return JSONResponse({ 'eliminado': False })
    
    archivo.delete()
    return JSONResponse({ 'eliminado': True })
