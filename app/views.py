from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BikeModel, Bike, BikeOwnership, BatteryModel, Battery, BatteryStatus, Station, SwapEvent, RideEvent, Trip
from .serializers import (
    BikeModelSerializer, BikeSerializer, BikeOwnershipSerializer,
    BatteryModelSerializer, BatterySerializer, BatteryStatusSerializer,
    StationSerializer, SwapEventSerializer, RideEventSerializer, TripSerializer
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

class StartTrip(APIView):
    def post(self, request):
        try:
            bike_id = request.data['bike_id']
            battery_id = request.data['battery_id']
            start_timestamp = request.data['timestamp']
        except KeyError as e:
            return Response({'error': f'Missing required parameter: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            trip = Trip.objects.create(
                bike_id=bike_id,
                battery_id=battery_id,
                start_timestamp=start_timestamp
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'trip_id': trip.id}, status=status.HTTP_201_CREATED)

class EndTrip(APIView):
    def put(self, request):
        try:
            trip_id = request.data['trip_id']
            end_timestamp = request.data['timestamp']
            distance_travelled = request.data['distance_travelled']
            energy_consumed = request.data['energy_consumed']
        except KeyError as e:
            return Response({'error': f'Missing required parameter: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            trip = Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            return Response({'error': f'Trip with id {trip_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

        trip.end_timestamp = end_timestamp
        trip.distance_travelled = distance_travelled
        trip.energy_consumed = energy_consumed

        try:
            trip.save()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'trip_id': trip.id})
    
class RideEvent(APIView):
    def post(self, request):
        try:
            trip_id = request.data['trip_id']
            timestamp = request.data['timestamp']
            fault_code = request.data['fault_code']
            system_fault = request.data['system_fault']
            ride_status = request.data['ride_status']
            speed = request.data['speed']
            gear = request.data['gear']
            latitude = request.data['latitude']
            longitude = request.data['longitude']
            capacity = request.data['capacity']
            temperature = request.data['temperature']
            voltage = request.data['voltage']
            current = request.data['current']
            charge = request.data['charge']
            battery_status = request.data['battery_status']

        except KeyError as e:
            return Response({'error': f'Missing required parameter: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ride_event = RideEvent.objects.create(
                trip_id=trip_id,
                timestamp=timestamp,
                fault_code=fault_code,
                system_fault=system_fault,
                status=ride_status,
                speed=speed,
                gear=gear,
                latitude=latitude,
                longitude=longitude
            )
            battery_id = Trip.objects.get(id=trip_id).battery_id
            battery_status = BatteryStatus.objects.create(
                battery_id=battery_id,
                trip_id=trip_id,
                timestamp=timestamp,
                capacity=capacity,
                temperature=temperature,
                voltage=voltage,
                current=current,
                charge=charge,
                status=battery_status
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'ride_event_id': ride_event.id}, status=status.HTTP_201_CREATED)
    
class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer