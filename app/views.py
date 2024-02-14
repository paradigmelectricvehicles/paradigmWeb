from rest_framework import generics
from .models import BikeModel, Bike, BikeOwnership, BatteryModel, Battery, BatteryStatus, Station, SwapEvent, RideEvent
from .serializers import (
    BikeModelSerializer, BikeSerializer, BikeOwnershipSerializer,
    BatteryModelSerializer, BatterySerializer, BatteryStatusSerializer,
    StationSerializer, SwapEventSerializer, RideEventSerializer
)

class BikeModelList(generics.ListCreateAPIView):
    queryset = BikeModel.objects.all()
    serializer_class = BikeModelSerializer

class BikeList(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

class BikeOwnershipList(generics.ListCreateAPIView):
    queryset = BikeOwnership.objects.all()
    serializer_class = BikeOwnershipSerializer

class BatteryModelList(generics.ListCreateAPIView):
    queryset = BatteryModel.objects.all()
    serializer_class = BatteryModelSerializer

class BatteryList(generics.ListCreateAPIView):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer

class BatteryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer

class BatteryStatusList(generics.ListCreateAPIView):
    queryset = BatteryStatus.objects.all()
    serializer_class = BatteryStatusSerializer

class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class SwapEventList(generics.ListCreateAPIView):
    queryset = SwapEvent.objects.all()
    serializer_class = SwapEventSerializer

class RideEventList(generics.ListCreateAPIView):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
