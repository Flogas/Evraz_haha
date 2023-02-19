from django.db import models


# Данные модели используются для сохранения данных получаемых с Kafka


class Bearing(models.Model):  # Подшипник базовый
    temperature_value = models.DecimalField(verbose_name="Температура", max_digits=6, decimal_places=2, null=True)
    temperature_warning_min = models.IntegerField(verbose_name="Уставка предупреждения (min)", null=True)
    temperature_warning_max = models.IntegerField(verbose_name="Уставка предупреждения (max)", null=True)
    temperature_alarm_min = models.IntegerField(verbose_name="Уставка аварийная (min)", null=True)
    temperature_alarm_max = models.IntegerField(verbose_name="Уставка аварийная (max)", null=True)

    def __str__(self):
        return 'Подшипник'

    class Meta:
        verbose_name = "Подшипник"
        verbose_name_plural = "Подшипники"


class BearingExtended(models.Model):  # Подшипник расширенный
    temperature_value = models.DecimalField(verbose_name="Температура", max_digits=6, decimal_places=2, null=True)
    temperature_warning_min = models.IntegerField(verbose_name="Уставка предупреждения (min)", null=True)
    temperature_warning_max = models.IntegerField(verbose_name="Уставка предупреждения (max)", null=True)
    temperature_alarm_min = models.IntegerField(verbose_name="Уставка аварийная (min)", null=True)
    temperature_alarm_max = models.IntegerField(verbose_name="Уставка аварийная (max)", null=True)

    vibration_axial_value = models.DecimalField(verbose_name="Вибрация Осевая", max_digits=12, decimal_places=10, null=True)
    vibration_axial_warning_min = models.DecimalField(verbose_name="Уставка предупреждения (min)", max_digits=12, decimal_places=10, null=True)
    vibration_axial_warning_max = models.DecimalField(verbose_name="Уставка предупреждения (max)", max_digits=12, decimal_places=10, null=True)
    vibration_axial_alarm_min = models.DecimalField(verbose_name="Уставка аварийная (min)", max_digits=12, decimal_places=10, null=True)
    vibration_axial_alarm_max = models.DecimalField(verbose_name="Уставка аварийная (max)", max_digits=12, decimal_places=10, null=True)

    vibration_horizontal_value = models.DecimalField(verbose_name="Вибрация Осевая", max_digits=12, decimal_places=10, null=True)
    vibration_horizontal_warning_min = models.DecimalField(verbose_name="Уставка предупреждения (min)", max_digits=12, decimal_places=10, null=True)
    vibration_horizontal_warning_max = models.DecimalField(verbose_name="Уставка предупреждения (max)", max_digits=12, decimal_places=10, null=True)
    vibration_horizontal_alarm_min = models.DecimalField(verbose_name="Уставка аварийная (min)", max_digits=12, decimal_places=10, null=True)
    vibration_horizontal_alarm_max = models.DecimalField(verbose_name="Уставка аварийная (max)", max_digits=12, decimal_places=10, null=True)

    vibration_vertical_value = models.DecimalField(verbose_name="Вибрация Осевая", max_digits=12, decimal_places=10)
    vibration_vertical_warning_min = models.DecimalField(verbose_name="Уставка предупреждения (min)", max_digits=12, decimal_places=10, null=True)
    vibration_vertical_warning_max = models.DecimalField(verbose_name="Уставка предупреждения (max)", max_digits=12, decimal_places=10, null=True)
    vibration_vertical_alarm_min = models.DecimalField(verbose_name="Уставка аварийная (min)", max_digits=12, decimal_places=10, null=True)
    vibration_vertical_alarm_max = models.DecimalField(verbose_name="Уставка аварийная (max)", max_digits=12, decimal_places=10, null=True)

    def __str__(self):
        return 'Подшипник'

    class Meta:
        verbose_name = "Подшипник расширенный"
        verbose_name_plural = "Подшипники расширенные"


class Cooler(models.Model):  # Охладитель
    oil_temperature_after = models.DecimalField(verbose_name="Температура масла после охладителя", max_digits=12, decimal_places=9, null=True)
    oil_temperature_before = models.DecimalField(verbose_name="Температура масла до охладителя", max_digits=12, decimal_places=9, null=True)
    water_temperature_after = models.DecimalField(verbose_name="Температура воды на выходе охладителя", max_digits=12, decimal_places=9, null=True)
    water_temperature_before = models.DecimalField(verbose_name="Температура воды до охладителя", max_digits=12, decimal_places=9, null=True)

    class Meta:
        verbose_name = "Охладитель"
        verbose_name_plural = "Охладители"


class Exhauster(models.Model):  # Эксгаустер
    name = models.CharField(verbose_name="Название эксгаустера", max_length=32)
    timestamp = models.DateTimeField(verbose_name="Отметка времени фиксации значений", editable=False)

    # Подшипники
    bearing_ext_one = models.OneToOneField('BearingExtended', verbose_name="Подшипник 1", on_delete=models.PROTECT, related_name="bearing_ext_one")
    bearing_ext_two = models.OneToOneField('BearingExtended', verbose_name="Подшипник 2", on_delete=models.PROTECT, related_name="bearing_ext_two")
    bearing_three = models.OneToOneField('Bearing', verbose_name="Подшипник 3", on_delete=models.PROTECT, related_name="bearing_three")
    bearing_four = models.OneToOneField('Bearing', verbose_name="Подшипник 4", on_delete=models.PROTECT, related_name="bearing_four")
    bearing_five = models.OneToOneField('Bearing', verbose_name="Подшипник 5", on_delete=models.PROTECT, related_name="bearing_five")
    bearing_six = models.OneToOneField('Bearing', verbose_name="Подшипник 6", on_delete=models.PROTECT, related_name="bearing_six")
    bearing_ext_seven = models.OneToOneField('BearingExtended', verbose_name="Подшипник 7", on_delete=models.PROTECT, related_name="bearing_ext_seven")
    bearing_ext_eight = models.OneToOneField('BearingExtended', verbose_name="Подшипник 8", on_delete=models.PROTECT, related_name="bearing_ext_eight")
    bearing_nine = models.OneToOneField('Bearing', verbose_name="Подшипник 9", on_delete=models.PROTECT, related_name="bearing_nine")

    # Охладитель
    cooler = models.OneToOneField('Cooler', verbose_name="Охладитель", on_delete=models.PROTECT)

    # Газовый коллектор
    gas_collector_temperature_before = models.DecimalField(verbose_name="Температура перед эксгаустером", max_digits=12, decimal_places=9, null=True)
    gas_collector_underpressure_before = models.DecimalField(verbose_name="Разрежение перед эксгаустером", max_digits=12, decimal_places=9, null=True)

    # Положение задвижки
    gas_valve_closed = models.BooleanField(verbose_name="ЗАКРЫТО задвижка газ эксгаустер", null=True)
    gas_valve_open = models.BooleanField(verbose_name="ОТКРЫТО задвижка газ эксгаустер", null=True)
    gas_valve_position = models.IntegerField(verbose_name="Положение задвижки газ эксгаустера", null=True)

    # Главный привод
    main_drive_rotor_current = models.IntegerField(verbose_name="Ток ротора эксгаустера", null=True)
    main_drive_rotor_voltage = models.IntegerField(verbose_name="Напряжение ротора эксгаустера", null=True)
    main_drive_stator_current = models.IntegerField(verbose_name="Ток статора эксгаустера", null=True)
    main_drive_stator_voltage = models.IntegerField(verbose_name="Напряжение статора эксгаустера", null=True)

    # Маслосистема
    oilsystem_oil_level = models.IntegerField(verbose_name="Уровень масла в маслосистеме эксгаустера", null=True)
    oilsystem_oil_pressure = models.IntegerField(verbose_name="Давление масла в маслосистеме эксгаустера", null=True)

    work_status = models.BooleanField(verbose_name="Работа эксгаустера", null=True)

    class Meta:
        verbose_name = "Эксгаустер"
        verbose_name_plural = "Эксгаустеры"
