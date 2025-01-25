from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Factory
from .serializers import FactorySerializer

class FactoryListView(APIView):
    def get(self, request):
        factories = Factory.objects.all()
        serializer = FactorySerializer(factories, many=True)
        return Response(serializer.data)

class FactoryDetailView(APIView):
    def get(self, request, pk):
        try:
            factory = Factory.objects.get(pk=pk)
            serializer = FactorySerializer(factory)
            return Response(serializer.data)
        except Factory.DoesNotExist:
            return Response({'error': 'Factory not found'}, status=404)
        
def map_view(request):
    return render(request, 'map.html')