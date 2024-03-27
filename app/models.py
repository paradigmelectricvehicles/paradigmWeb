from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class BikeModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    version = models.SmallIntegerField()
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Bike(models.Model):
    number = models.CharField(max_length=17, unique=True, db_index=True)
    bike_model = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    license_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    owner = models.ManyToManyField(User, through="BikeOwnership", through_fields=('bike', 'owner'))
    battery_ids = ArrayField(models.PositiveBigIntegerField(), size=2, default=list, blank=True)

    def __str__(self):
        return str(self.license_number)

    @property
    def current_owner(self):
        return BikeOwnership.objects.filter(bike=self, sell_date=None).last

    @property
    def last_trip(self):
        return Trip.objects.filter(bike=self).latest('start_timestamp').start_timestamp
    
    @property
    def batteries(self):
        return Battery.objects.filter(id__in=self.battery_ids)
    
    @property
    def location(self):
        rideevent = RideEvent.objects.filter(trip__bike=self).latest('timestamp')
        return { "latitude": rideevent.latitude, "longitude": rideevent.longitude, "located_at": rideevent.timestamp } if rideevent else None


class BikeOwnership(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_date = models.DateField()
    sell_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.owner.username


class BatteryModel(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.DecimalField(max_digits=6, decimal_places=3)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    type = models.CharField(max_length=50)
    version = models.SmallIntegerField()
    manufacturer = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Battery(models.Model):
    number = models.CharField(max_length=17, unique=True, db_index=True)
    battery_model = models.ForeignKey(BatteryModel, on_delete=models.CASCADE)
    distance_travelled = models.PositiveIntegerField(default=0)
    energy_consumed = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    status = models.CharField(max_length=10)
    manufacturing_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.battery_model.name + " " + str(self.manufacturing_date) + " " + str(self.id)

    @property
    def asset(self):
        swap_event = SwapEvent.objects.filter(battery=self).latest('timestamp')
        return swap_event.station if swap_event.station else swap_event.bike

    @property
    def asset_type(self):
        swap_event = SwapEvent.objects.filter(battery=self).latest('timestamp')
        return "Station" if swap_event.station else "Bike"


class Station(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(null=True, blank=True)
    battery_ids = ArrayField(models.PositiveBigIntegerField(), size=12, default=list, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def batteries(self):
        return Battery.objects.filter(id__in=self.battery_ids)
    
    @property
    def last_used(self):
        return SwapEvent.objects.filter(station=self).latest('timestamp').timestamp


class SwapEvent(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(db_index=True)
    event_type = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="station_or_bike",
                check=(
                    models.Q(station_id__isnull=True, bike_id__isnull=False)
                    | models.Q(station_id__isnull=False, bike_id__isnull=True)
                ),
            )
        ]

    def __str__(self):
        return self.battery.battery_model.name + " " + str(self.timestamp) + " " + self.event_type


class Trip(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField(null=True, blank=True)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    distance_travelled = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    energy_consumed = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.bike) + " " + str(self.id)

    @property
    def status(self):
        return "Ongoing" if self.end_timestamp is None else "Completed"
    
    @property
    def start_location(self):
        rideevent = RideEvent.objects.filter(trip=self).earliest('timestamp')
        return (rideevent.latitude, rideevent.longitude) if rideevent else None

    @property
    def end_location(self):
        rideevent = RideEvent.objects.filter(trip=self).latest('timestamp')
        return (rideevent.latitude, rideevent.longitude) if rideevent else None


class RideEvent(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    fault_code = models.CharField(max_length=10)
    system_fault = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    gear = models.SmallIntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.trip.id) + " " + str(self.timestamp)


class BatteryStatus(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    capacity = models.DecimalField(max_digits=6, decimal_places=3)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    voltage = models.DecimalField(max_digits=5, decimal_places=2)
    current = models.DecimalField(max_digits=5, decimal_places=2)
    charge = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True)
