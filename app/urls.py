from django.urls import path
from .views import (
    BikeModelList, BikeList, BikeDetail, BikeOwnershipList,
    BatteryModelList, BatteryList, BatteryDetail, BatteryStatusList,
    StationList, SwapEventList,
    RideEventList, StartTrip, EndTrip, RideEvent
)

app_name = 'app'

urlpatterns = [
    # Bike App URLs
    path('bikemodels/', BikeModelList.as_view(), name='bikemodel-list'),
    path('bikes/', BikeList.as_view(), name='bike-list'),
    path('bikes/<int:pk>/', BikeDetail.as_view(), name='bike-detail'),
    path('bikeownerships/', BikeOwnershipList.as_view(), name='bikeownership-list'),

    # Battery App URLs
    path('batterymodels/', BatteryModelList.as_view(), name='batterymodel-list'),
    path('batteries/', BatteryList.as_view(), name='battery-list'),
    path('batteries/<int:pk>/', BatteryDetail.as_view(), name='battery-detail'),
    path('batterystatus/', BatteryStatusList.as_view(), name='batterystatus-list'),

    # Station and SwapEvent App URLs
    path('stations/', StationList.as_view(), name='station-list'),
    path('swapevents/', SwapEventList.as_view(), name='swapevent-list'),

    # RideEvent App URLs
    path('rideevents/', RideEventList.as_view(), name='rideevent-list'),
    path('starttrip/', StartTrip.as_view(), name='start-trip'),
    path('endtrip/', EndTrip.as_view(), name='end-trip'),
    path('rideevent/', RideEvent.as_view(), name='rideevent-list'),
]
