from django.db import models

# Create your models here.
from django.db import models


# Данные модели используются для регистрации эксгаустеров как объектов

class BearingObj(models.Model):  # Подшипник базовый
    temperature_value = models.CharField(verbose_name="Температура", max_length=32)
    temperature_alarm_max = models.CharField(verbose_name="Уставка аварийная (max)", max_length=32)
    temperature_alarm_min = models.CharField(verbose_name="Уставка аварийная (min)", max_length=32)
    temperature_warning_max = models.CharField(verbose_name="Уставка предупреждения (max)", max_length=32)
    temperature_warning_min = models.CharField(verbose_name="Уставка предупреждения (min)", max_length=32)

    def __str__(self):
        return "Подшипник"

    class Meta:
        verbose_name = "Подшипник"
        verbose_name_plural = "Подшипники"


class BearingExtendedObj(models.Model):  # Подшипник расширенный
    temperature_value = models.CharField(verbose_name="Температура", max_length=32)
    temperature_alarm_max = models.CharField(verbose_name="Уставка аварийная (max)", max_length=32)
    temperature_alarm_min = models.CharField(verbose_name="Уставка аварийная (min)", max_length=32)
    temperature_warning_max = models.CharField(verbose_name="Уставка предупреждения (max)", max_length=32)
    temperature_warning_min = models.CharField(verbose_name="Уставка предупреждения (min)", max_length=32)

    vibration_axial_value = models.CharField(verbose_name="Вибрация Осевая", max_length=32)
    vibration_axial_alarm_max = models.CharField(verbose_name="Уставка аварийная (max)", max_length=32)
    vibration_axial_alarm_min = models.CharField(verbose_name="Уставка аварийная (min)", max_length=32)
    vibration_axial_warning_max = models.CharField(verbose_name="Уставка предупреждения (max)", max_length=32)
    vibration_axial_warning_min = models.CharField(verbose_name="Уставка предупреждения (min)", max_length=32)

    vibration_horizontal_value = models.CharField(verbose_name="Вибрация Горизонтальная", max_length=32)
    vibration_horizontal_alarm_max = models.CharField(verbose_name="Уставка аварийная (max)", max_length=32)
    vibration_horizontal_alarm_min = models.CharField(verbose_name="Уставка аварийная (min)", max_length=32)
    vibration_horizontal_warning_max = models.CharField(verbose_name="Уставка предупреждения (max)", max_length=32)
    vibration_horizontal_warning_min = models.CharField(verbose_name="Уставка предупреждения (min)", max_length=32)

    vibration_vertical_value = models.CharField(verbose_name="Вибрация Вертикальная", max_length=32)
    vibration_vertical_alarm_max = models.CharField(verbose_name="Уставка аварийная (max)", max_length=32)
    vibration_vertical_alarm_min = models.CharField(verbose_name="Уставка аварийная (min)", max_length=32)
    vibration_vertical_warning_max = models.CharField(verbose_name="Уставка предупреждения (max)", max_length=32)
    vibration_vertical_warning_min = models.CharField(verbose_name="Уставка предупреждения (min)", max_length=32)

    class Meta:
        verbose_name = "Подшипник расширенный"
        verbose_name_plural = "Подшипники расширенные"


class CoolerObj(models.Model):  # Охладитель
    oil_temperature_after = models.CharField(verbose_name="Температура масла после охладителя", max_length=32)
    oil_temperature_before = models.CharField(verbose_name="Температура масла до охладителя", max_length=32)
    water_temperature_after = models.CharField(verbose_name="Температура воды на выходе охладителя", max_length=32)
    water_temperature_before = models.CharField(verbose_name="Температура воды до охладителя", max_length=32)

    class Meta:
        verbose_name = "Охладитель"
        verbose_name_plural = "Охладители"


class ExhausterObj(models.Model):  # Эксгаустер

    name = models.CharField(verbose_name="Название эксгаустера", max_length=32)

    # Подшипники
    bearing_ext_one = models.OneToOneField('BearingExtendedObj', verbose_name="Подшипник 1", on_delete=models.PROTECT, related_name="bearing_ext_one")
    bearing_ext_two = models.OneToOneField('BearingExtendedObj', verbose_name="Подшипник 2", on_delete=models.PROTECT, related_name="bearing_ext_two")
    bearing_three = models.OneToOneField('BearingObj', verbose_name="Подшипник 3", on_delete=models.PROTECT, related_name="bearing_three")
    bearing_four = models.OneToOneField('BearingObj', verbose_name="Подшипник 4", on_delete=models.PROTECT, related_name="bearing_four")
    bearing_five = models.OneToOneField('BearingObj', verbose_name="Подшипник 5", on_delete=models.PROTECT, related_name="bearing_five")
    bearing_six = models.OneToOneField('BearingObj', verbose_name="Подшипник 6", on_delete=models.PROTECT, related_name="bearing_six")
    bearing_ext_seven = models.OneToOneField('BearingExtendedObj', verbose_name="Подшипник 7", on_delete=models.PROTECT, related_name="bearing_ext_seven")
    bearing_ext_eight = models.OneToOneField('BearingExtendedObj', verbose_name="Подшипник 8", on_delete=models.PROTECT, related_name="bearing_ext_eight")
    bearing_nine = models.OneToOneField('BearingObj', verbose_name="Подшипник 9", on_delete=models.PROTECT, related_name="bearing_nine")

    # Охладитель
    cooler = models.OneToOneField('CoolerObj', verbose_name="Охладитель", on_delete=models.PROTECT)

    # Газовый коллектор
    gas_collector_temperature_before = models.CharField(verbose_name="Температура перед эксгаустером", max_length=32)
    gas_collector_underpressure_before = models.CharField(verbose_name="Разрежение перед эксгаустером", max_length=32)

    # Положение задвижки
    gas_valve_closed = models.CharField(verbose_name="ЗАКРЫТО задвижка газ эксгаустер", max_length=32)
    gas_valve_open = models.CharField(verbose_name="ОТКРЫТО задвижка газ эксгаустер", max_length=32)
    gas_valve_position = models.CharField(verbose_name="Положение задвижки газ эксгаустера", max_length=32)

    # Главный привод
    main_drive_rotor_current = models.CharField(verbose_name="Ток ротора эксгаустера", max_length=32)
    main_drive_rotor_voltage = models.CharField(verbose_name="Напряжение ротора эксгаустера", max_length=32)
    main_drive_stator_current = models.CharField(verbose_name="Ток статора эксгаустера", max_length=32)
    main_drive_stator_voltage = models.CharField(verbose_name="Напряжение статора эксгаустера", max_length=32)

    # Маслосистема
    oilsystem_oil_level = models.CharField(verbose_name="Уровень масла в маслосистеме эксгаустера", max_length=32)
    oilsystem_oil_pressure = models.CharField(verbose_name="Давление масла в маслосистеме эксгаустера", max_length=32)

    work_status = models.CharField(verbose_name="Работа эксгаустера", max_length=32)

    class Meta:
        verbose_name = "Эксгаустер"
        verbose_name_plural = "Эксгаустеры"
