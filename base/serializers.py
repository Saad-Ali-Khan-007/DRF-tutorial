from rest_framework.serializers import ModelSerializer
from .models import Advocate

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        field = '__all__'