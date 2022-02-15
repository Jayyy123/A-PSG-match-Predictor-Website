from urllib import request
from rest_framework.serializers import ModelSerializer
from predictor.models import PsgPredictor


class PredictorS(ModelSerializer):
    class Meta:
        model = PsgPredictor
        fields = '__all__'

