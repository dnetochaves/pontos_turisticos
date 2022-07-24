from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from core.api.serializers import PontosTuristicosSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PontosTuristicosSerializer
    queryset = PontosTuristicos.objects.all()
