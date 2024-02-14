# your_project/your_app/serializers.py
from rest_framework.serializers import ModelSerializer
from .models import BikeModel, Bike, BikeOwnership, BatteryModel, Battery, BatteryStatus, Station, SwapEvent, RideEvent

class BikeModelSerializer(ModelSerializer):
    class Meta:
        model = BikeModel
        fields = '__all__'

class BikeOwnershipSerializer(ModelSerializer):
    class Meta:
        model = BikeOwnership
        fields = '__all__'

class BikeSerializer(ModelSerializer):
    owner = BikeOwnershipSerializer(many=True, read_only=True)

    class Meta:
        model = Bike
        fields = '__all__'

class BatteryModelSerializer(ModelSerializer):
    class Meta:
        model = BatteryModel
        fields = '__all__'

class BatterySerializer(ModelSerializer):
    class Meta:
        model = Battery
        fields = '__all__'

class BatteryStatusSerializer(ModelSerializer):
    class Meta:
        model = BatteryStatus
        fields = '__all__'

class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class SwapEventSerializer(ModelSerializer):
    class Meta:
        model = SwapEvent
        fields = '__all__'

class RideEventSerializer(ModelSerializer):
    class Meta:
        model = RideEvent
        fields = '__all__'
