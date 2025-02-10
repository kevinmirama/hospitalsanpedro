from rest_framework import viewsets
from .models import Universidad, Documento
from .serializers import UniversidadSerializer, DocumentoSerializer
from rest_framework.response import Response


class UniversidadViewSet(viewsets.ModelViewSet):
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def get_queryset(self):
        universidad_id = self.request.query_params.get('universidad_id')
        if universidad_id:
            return Documento.objects.filter(universidad_id=universidad_id)
        return Documento.objects.all()
