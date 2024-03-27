from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import BikeModel, Bike, BikeOwnership, BatteryModel, Battery, BatteryStatus, Station, SwapEvent, RideEvent, Trip

@admin.register(BikeModel)
class BikeModelAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "version", "release_date")
    list_filter = ("name", "price", "version", ("release_date", DateRangeFilter))

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ("number", "bike_model", "manufacturing_date", "license_number", "current_owner")
    list_filter = ("bike_model", ("manufacturing_date", DateRangeFilter))

@admin.register(BikeOwnership)
class BikeOwnershipAdmin(admin.ModelAdmin):
    list_display = ("bike", "owner", "buy_date", "sell_date")
    list_filter = ("bike", "owner", ("buy_date", DateRangeFilter), ("sell_date", DateRangeFilter))


@admin.register(BatteryModel)
class BatteryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "weight", "type", "version", "manufacturer")
    list_filter = ("name", "capacity", "weight", "type", "version", "manufacturer")

@admin.register(Battery)
class BatteryAdmin(admin.ModelAdmin):
    list_display = ("number", "battery_model", "status", "manufacturing_date")
    list_filter = ("battery_model", "status", ("manufacturing_date", DateRangeFilter))

@admin.register(BatteryStatus)
class BatteryStatusAdmin(admin.ModelAdmin):
    list_display = ("battery", "timestamp", "status", "temperature", "voltage", "current", "trip", "station")
    list_filter = ("battery", "status", ("timestamp", DateTimeRangeFilter))

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude")
    list_filter = ("name",)

@admin.register(SwapEvent)
class SwapEventAdmin(admin.ModelAdmin):
    list_display = ("battery", "station", "bike", "timestamp", "event_type")
    list_filter = ("battery", "station", "bike", "event_type", ("timestamp", DateTimeRangeFilter))

@admin.register(RideEvent)
class RideEventAdmin(admin.ModelAdmin):
    list_display = ("trip", "timestamp", "fault_code", "speed", "latitude", "longitude")
    list_filter = ("trip", ("timestamp", DateTimeRangeFilter))

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("bike", "start_timestamp", "end_timestamp", "battery", "distance_travelled", "energy_consumed")
    list_filter = ("bike", ("start_timestamp", DateTimeRangeFilter), ("end_timestamp", DateTimeRangeFilter), "battery")