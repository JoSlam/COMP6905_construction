from datetime import datetime
import random
import time
from sensorAPI import getNitrogenMeasurement, getParticulateMatterMeasurement, ParticulateMatterType

print("Simulator bootstrap time: {0}".format(time.time()))

site_locations = ["North", "South", "East", "West", "Central"]


while True:
    record_time = time.time()
    location = random.choice(site_locations)

    print("\nLocation: {0}".format(location))
    print("\nBeginning measurements: {0}".format(record_time))

    # get some random data
    nitrogen_concentration = getNitrogenMeasurement()
    print("\nCurrent NO2 concentration: {0}".format(nitrogen_concentration))

    fine_concentration = getParticulateMatterMeasurement(
        ParticulateMatterType.Fine)
    print("\nCurrent PM 2.5 concentration: {0}".format(fine_concentration))

    coarse_concentration = getParticulateMatterMeasurement(
        ParticulateMatterType.Coarse)
    print("\nCurrent PM 10 concentration: {0}".format(coarse_concentration))

    # create data payload
    data_payload = {
        "location": location,
        "timestamp": record_time,
        "concentration_readings": {
            "no2_concentration": nitrogen_concentration,
            "fine_pm_concentration": fine_concentration,
            "coarse_pm_concentration": coarse_concentration
        }
    }

    # connect to IoT gateway
    # send data

    # Sleep thread for 10 minutes
    time.sleep(600)
