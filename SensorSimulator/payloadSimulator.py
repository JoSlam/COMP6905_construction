import random
import time
from math import trunc
from sensorAPI import getNitrogenMeasurement, getParticulateMatterMeasurement, ParticulateMatterType

device_ids = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5"]


def getDataPayload():
    record_time = trunc(time.time())
    selected_device = random.choice(device_ids)

    print("\Device ID: {0}".format(selected_device))
    print("\nBeginning measurements: {0}".format(record_time))

    # get some random data
    nitrogen_concentration = getNitrogenMeasurement()
    # print("\nCurrent NO2 concentration: {0}".format(nitrogen_concentration))

    fine_concentration = getParticulateMatterMeasurement(
        ParticulateMatterType.Fine)
    # print("\nCurrent PM 2.5 concentration: {0}".format(fine_concentration))

    coarse_concentration = getParticulateMatterMeasurement(
        ParticulateMatterType.Coarse)
    # print("\nCurrent PM 10 concentration: {0}".format(coarse_concentration))

    # create data payload
    data_payload = {
        "device_id": selected_device,
        "timestamp": record_time,
        "no2_concentration": str(nitrogen_concentration),
        "fine_pm_concentration": str(fine_concentration),
        "coarse_pm_concentration": str(coarse_concentration)
    }

    return data_payload
