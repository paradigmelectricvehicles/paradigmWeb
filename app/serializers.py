from rest_framework.serializers import ModelSerializer, StringRelatedField, ReadOnlyField
from .models import BikeModel, Bike, BikeOwnership, BatteryModel, Battery, BatteryStatus, Station, SwapEvent, RideEvent, Trip


class BikeModelSerializer(ModelSerializer):
    class Meta:
        model = BikeModel
        fields = '__all__'


class BikeOwnershipSerializer(ModelSerializer):
    class Meta:
        model = BikeOwnership
        fields = '__all__'


class TripSerializer(ModelSerializer):
    bike = StringRelatedField()
    battery = StringRelatedField()
    status = ReadOnlyField()
    start_location = ReadOnlyField()
    end_location = ReadOnlyField()

    class Meta:
        model = Trip
        fields = '__all__'


class BikeSerializer(ModelSerializer):
    current_owner = StringRelatedField()
    last_trip = TripSerializer()
    batteries = StringRelatedField(many=True)
    bike_model = StringRelatedField()
    location = ReadOnlyField()

    class Meta:
        model = Bike
        fields = '__all__'


class BatteryModelSerializer(ModelSerializer):
    class Meta:
        model = BatteryModel
        fields = '__all__'


class BatterySerializer(ModelSerializer):
    asset = StringRelatedField()
    asset_type = ReadOnlyField()

    class Meta:
        model = Battery
        fields = '__all__'


class BatteryStatusSerializer(ModelSerializer):
    class Meta:
        model = BatteryStatus
        fields = '__all__'


class StationSerializer(ModelSerializer):
    batteries = StringRelatedField(many=True)
    last_used = ReadOnlyField()

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
