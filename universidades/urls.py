from django.urls import path, include
from rest_framework.routers import DefaultRouter
from universidades.views import UniversidadViewSet, DocumentoViewSet

router = DefaultRouter()
router.register(r'universidades', UniversidadViewSet)
router.register(r'documentos', DocumentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
