# Generated by Django 4.2.9 on 2024-02-15 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_battery_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batterystatus',
            name='ride_event',
        ),
        migrations.RemoveField(
            model_name='rideevent',
            name='bike',
        ),
        migrations.AddField(
            model_name='battery',
            name='distance_travelled',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battery',
            name='energy_consumed',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='batterymodel',
            name='capacity',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='batterymodel',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('distance_travelled', models.DecimalField(decimal_places=2, max_digits=5)),
                ('energy_consumed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.battery')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bike')),
            ],
        ),
        migrations.AddField(
            model_name='batterystatus',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.trip'),
        ),
        migrations.AddField(
            model_name='rideevent',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.trip'),
            preserve_default=False,
        ),
    ]
