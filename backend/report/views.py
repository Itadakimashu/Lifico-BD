from rest_framework import viewsets

from .serializers import ReportSerializer, SymtomSerializer
# Create your views here.

from .models import Report, Symtom

class SymtomViewSet(viewsets.ModelViewSet):
    queryset = Symtom.objects.all()
    serializer_class = SymtomSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
        


