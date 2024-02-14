# Generated by Django 4.2.9 on 2024-02-06 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(max_length=10)),
                ('manufacturing_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BatteryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('type', models.CharField(max_length=50)),
                ('version', models.SmallIntegerField()),
                ('manufacturer', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturing_date', models.DateField()),
                ('description', models.TextField()),
                ('license_plate', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('version', models.SmallIntegerField()),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SwapEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('event_type', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.battery')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bike')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.station')),
            ],
        ),
        migrations.CreateModel(
            name='RideEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('fault_code', models.CharField(max_length=10)),
                ('system_fault', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('distanceTravelled', models.DecimalField(decimal_places=2, max_digits=5)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gear', models.SmallIntegerField()),
                ('energyConsumed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bike')),
            ],
        ),
        migrations.CreateModel(
            name='BikeOwnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateField()),
                ('sell_date', models.DateField(blank=True, null=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bike')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='bike_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bikemodel'),
        ),
        migrations.AddField(
            model_name='bike',
            name='owner',
            field=models.ManyToManyField(through='app.BikeOwnership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BatteryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('health', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('voltage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('current', models.DecimalField(decimal_places=2, max_digits=5)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('charging_status', models.CharField(max_length=10)),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.battery')),
                ('ride_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.rideevent')),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.station')),
            ],
        ),
        migrations.AddField(
            model_name='battery',
            name='battery_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.batterymodel'),
        ),
    ]
