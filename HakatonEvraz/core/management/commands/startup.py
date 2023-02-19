from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
from datamanager.models import *
from core.models import *
from json import loads
from datetime import datetime


def is_valid(sourse: dict, key: str):
    try:
        return sourse[key]
    except KeyError:
        return None


def return_bearing(bearing_obj, msg: dict):
    return Bearing.objects.create(
        temperature_value=is_valid(msg, bearing_obj.temperature_value),
        temperature_alarm_max=is_valid(msg, bearing_obj.temperature_alarm_max),
        temperature_alarm_min=is_valid(msg, bearing_obj.temperature_alarm_min),
        temperature_warning_max=is_valid(msg, bearing_obj.temperature_warning_max),
        temperature_warning_min=is_valid(msg, bearing_obj.temperature_warning_min),

    )


def return_bearing_ext(bearing_ext_obj, msg: dict):
    return BearingExtended.objects.create(
        temperature_value=is_valid(msg, bearing_ext_obj.temperature_value),
        temperature_alarm_max=is_valid(msg, bearing_ext_obj.temperature_alarm_max),
        temperature_alarm_min=is_valid(msg, bearing_ext_obj.temperature_alarm_min),
        temperature_warning_max=is_valid(msg, bearing_ext_obj.temperature_warning_max),
        temperature_warning_min=is_valid(msg, bearing_ext_obj.temperature_warning_min),

        vibration_axial_value=is_valid(msg, bearing_ext_obj.vibration_axial_value),
        vibration_axial_alarm_max=is_valid(msg, bearing_ext_obj.vibration_axial_alarm_max),
        vibration_axial_alarm_min=is_valid(msg, bearing_ext_obj.vibration_axial_alarm_min),
        vibration_axial_warning_max=is_valid(msg, bearing_ext_obj.vibration_axial_warning_max),
        vibration_axial_warning_min=is_valid(msg, bearing_ext_obj.vibration_axial_warning_min),

        vibration_horizontal_value=is_valid(msg, bearing_ext_obj.vibration_horizontal_value),
        vibration_horizontal_alarm_max=is_valid(msg, bearing_ext_obj.vibration_horizontal_alarm_max),
        vibration_horizontal_alarm_min=is_valid(msg, bearing_ext_obj.vibration_horizontal_alarm_min),
        vibration_horizontal_warning_max=is_valid(msg, bearing_ext_obj.vibration_horizontal_warning_max),
        vibration_horizontal_warning_min=is_valid(msg, bearing_ext_obj.vibration_horizontal_warning_min),

        vibration_vertical_value=is_valid(msg, bearing_ext_obj.vibration_vertical_value),
        vibration_vertical_alarm_max=is_valid(msg, bearing_ext_obj.vibration_vertical_alarm_max),
        vibration_vertical_alarm_min=is_valid(msg, bearing_ext_obj.vibration_vertical_alarm_min),
        vibration_vertical_warning_max=is_valid(msg, bearing_ext_obj.vibration_vertical_warning_max),
        vibration_vertical_warning_min=is_valid(msg, bearing_ext_obj.vibration_vertical_warning_min),
    )


def return_cooler(cooler_obj, msg: dict):
    return Cooler.objects.create(
        oil_temperature_after=is_valid(msg, cooler_obj.oil_temperature_after),
        oil_temperature_before=is_valid(msg, cooler_obj.oil_temperature_before),
        water_temperature_after=is_valid(msg, cooler_obj.water_temperature_after),
        water_temperature_before=is_valid(msg, cooler_obj.water_temperature_before),
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        consumer = KafkaConsumer(
            bootstrap_servers='rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091',
            sasl_mechanism='SCRAM-SHA-512',
            security_protocol='SASL_SSL',
            sasl_plain_username='9433_reader',
            sasl_plain_password='eUIpgWu0PWTJaTrjhjQD3.hoyhntiK',
            ssl_cafile=r"C:\Users\Вселенный\Desktop\HakatonEvraz\CA.pem",
            group_id='$Датамыши',
        )

        consumer.subscribe(['zsmk-9433-dev-01'])

        for message in consumer:
            msg = message.value
            msg_json = loads(msg.decode('utf-8'))  # .items()
            print(msg_json['moment'])
            for E in ExhausterObj.objects.all():
                record = Exhauster.objects.create(
                    name=E.name,
                    timestamp=datetime.strptime(msg_json['moment'], '%Y-%m-%dT%H:%M:%S.%f'),

                    bearing_ext_one=return_bearing_ext(E.bearing_ext_one, msg_json),
                    bearing_ext_two=return_bearing_ext(E.bearing_ext_two, msg_json),
                    bearing_three=return_bearing(E.bearing_three, msg_json),
                    bearing_four=return_bearing(E.bearing_four, msg_json),
                    bearing_five=return_bearing(E.bearing_five, msg_json),
                    bearing_six=return_bearing(E.bearing_six, msg_json),
                    bearing_ext_seven=return_bearing_ext(E.bearing_ext_seven, msg_json),
                    bearing_ext_eight=return_bearing_ext(E.bearing_ext_eight, msg_json),
                    bearing_nine=return_bearing(E.bearing_nine, msg_json),

                    cooler=return_cooler(E.cooler, msg_json),

                    gas_collector_temperature_before=is_valid(msg_json, E.gas_collector_temperature_before),
                    gas_collector_underpressure_before=is_valid(msg_json, E.gas_collector_underpressure_before),

                    gas_valve_closed=is_valid(msg_json, E.gas_valve_closed),
                    gas_valve_open=is_valid(msg_json, E.gas_valve_open),
                    gas_valve_position=is_valid(msg_json, E.gas_valve_position),

                    main_drive_stator_voltage=is_valid(msg_json, E.main_drive_stator_voltage),
                    main_drive_stator_current=is_valid(msg_json, E.main_drive_stator_current),
                    main_drive_rotor_voltage=is_valid(msg_json, E.main_drive_rotor_voltage),
                    main_drive_rotor_current=is_valid(msg_json, E.main_drive_rotor_current),

                    oilsystem_oil_pressure=is_valid(msg_json, E.oilsystem_oil_pressure),
                    oilsystem_oil_level=is_valid(msg_json, E.oilsystem_oil_level),

                    work_status=is_valid(msg_json, E.work_status),
                )
                print(record)

        # unsubscribe and close  consumer
        consumer.unsubscribe()
        consumer.close()
