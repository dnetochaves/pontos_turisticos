from rest_framework.serializers import ModelSerializer
from core.models import PontosTuristicos


class PontosTuristicosSerializer(ModelSerializer):
    class Meta:
        model = PontosTuristicos
        fields = ('__all__')
