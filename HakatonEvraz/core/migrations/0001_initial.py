# Generated by Django 4.1.7 on 2023-02-17 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_value', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Температура')),
                ('temperature_warning_min', models.IntegerField(verbose_name='Уставка предупреждения (min)')),
                ('temperature_warning_max', models.IntegerField(verbose_name='Уставка предупреждения (max)')),
                ('temperature_alarm_min', models.IntegerField(verbose_name='Уставка аварийная (min)')),
                ('temperature_alarm_max', models.IntegerField(verbose_name='Уставка аварийная (max)')),
            ],
            options={
                'verbose_name': 'Подшипник',
                'verbose_name_plural': 'Подшипники',
            },
        ),
        migrations.CreateModel(
            name='BearingExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_value', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Температура')),
                ('temperature_warning_min', models.IntegerField(verbose_name='Уставка предупреждения (min)')),
                ('temperature_warning_max', models.IntegerField(verbose_name='Уставка предупреждения (max)')),
                ('temperature_alarm_min', models.IntegerField(verbose_name='Уставка аварийная (min)')),
                ('temperature_alarm_max', models.IntegerField(verbose_name='Уставка аварийная (max)')),
                ('vibration_axial_value', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Вибрация Осевая')),
                ('vibration_axial_warning_min', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка предупреждения (min)')),
                ('vibration_axial_warning_max', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка предупреждения (max)')),
                ('vibration_axial_alarm_min', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка аварийная (min)')),
                ('vibration_axial_alarm_max', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка аварийная (max)')),
                ('vibration_horizontal_value', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Вибрация Осевая')),
                ('vibration_horizontal_warning_min', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка предупреждения (min)')),
                ('vibration_horizontal_warning_max', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка предупреждения (max)')),
                ('vibration_horizontal_alarm_min', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка аварийная (min)')),
                ('vibration_horizontal_alarm_max', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка аварийная (max)')),
                ('vibration_vertical_value', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Вибрация Осевая')),
                ('vibration_vertical_warning_min', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка предупреждения (min)')),
                ('vibration_vertical_warning_max', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка предупреждения (max)')),
                ('vibration_vertical_alarm_min', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка аварийная (min)')),
                ('vibration_vertical_alarm_max', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Уставка аварийная (max)')),
            ],
            options={
                'verbose_name': 'Подшипник расширенный',
                'verbose_name_plural': 'Подшипники расширенные',
            },
        ),
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oil_temperature_after', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Температура масла после охладителя')),
                ('oil_temperature_before', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Температура масла до охладителя')),
                ('water_temperature_after', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Температура воды на выходе охладителя')),
                ('water_temperature_before', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Температура воды до охладителя')),
            ],
            options={
                'verbose_name': 'Охладитель',
                'verbose_name_plural': 'Охладители',
            },
        ),
        migrations.CreateModel(
            name='Exhauster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название эксгаустера')),
                ('timestamp', models.DateTimeField(editable=False, verbose_name='Отметка времени фиксации значений')),
                ('gas_collector_temperature_before', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Температура перед эксгаустером')),
                ('gas_collector_underpressure_before', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Разрежение перед эксгаустером')),
                ('gas_valve_closed', models.BooleanField(verbose_name='ЗАКРЫТО задвижка газ эксгаустер')),
                ('gas_valve_open', models.BooleanField(verbose_name='ОТКРЫТО задвижка газ эксгаустер')),
                ('gas_valve_position', models.IntegerField(verbose_name='Положение задвижки газ эксгаустера')),
                ('main_drive_rotor_current', models.IntegerField(verbose_name='Ток ротора эксгаустера')),
                ('main_drive_rotor_voltage', models.IntegerField(verbose_name='Напряжение ротора эксгаустера')),
                ('main_drive_stator_current', models.IntegerField(verbose_name='Ток статора эксгаустера')),
                ('main_drive_stator_voltage', models.IntegerField(verbose_name='Напряжение статора эксгаустера')),
                ('oilsystem_oil_level', models.IntegerField(verbose_name='Уровень масла в маслосистеме эксгаустера')),
                ('oilsystem_oil_pressure', models.IntegerField(verbose_name='Давление масла в маслосистеме эксгаустера')),
                ('work_status', models.BooleanField(verbose_name='Работа эксгаустера')),
                ('bearing_ext_eight', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_ext_eight', to='core.bearingextended')),
                ('bearing_ext_one', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_ext_one', to='core.bearingextended')),
                ('bearing_ext_seven', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_ext_seven', to='core.bearingextended')),
                ('bearing_ext_two', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_ext_two', to='core.bearingextended')),
                ('bearing_five', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_five', to='core.bearing')),
                ('bearing_four', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_four', to='core.bearing')),
                ('bearing_nine', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_nine', to='core.bearing')),
                ('bearing_six', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_six', to='core.bearing')),
                ('bearing_three', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bearing_three', to='core.bearing')),
                ('cooler', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.cooler')),
            ],
            options={
                'verbose_name': 'Эксгаустер',
                'verbose_name_plural': 'Эксгаустеры',
            },
        ),
    ]
