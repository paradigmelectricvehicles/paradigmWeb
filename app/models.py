from django.db import models
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
    bike_model = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    license_plate = models.CharField(max_length=10, unique=True, null=True, blank=True)
    owner = models.ManyToManyField(User, through="BikeOwnership", through_fields=('bike', 'owner'))

    def __str__(self):
        return str(self.license_plate)
    

class BikeOwnership(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_date = models.DateField()
    sell_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.bike + " " + self.owner.username
    

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
    battery_model = models.ForeignKey(BatteryModel, on_delete=models.CASCADE)
    distance_travelled = models.PositiveIntegerField(default=0)
    energy_consumed = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    status = models.CharField(max_length=10)
    manufacturing_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.battery_model.name + " " + str(self.manufacturing_date) + " " + str(self.id)


class Station(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class SwapEvent(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField()
    event_type = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.battery.battery_model.name + " " + str(self.timestamp) + " " + self.event_type
    

class Trip(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField(null=True, blank=True)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    distance_travelled = models.DecimalField(max_digits=5, decimal_places=2)
    energy_consumed = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.bike) + " " + str(self.start_timestamp) + " " + str(self.end_timestamp)


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
        return str(self.bike) + " " + str(self.timestamp)


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

