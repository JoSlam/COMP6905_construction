import random
import time
from math import trunc
from sensorAPI import getNitrogenMeasurement, getParticulateMatterMeasurement, ParticulateMatterType, getRandomValue


sensor_locations = [
    {
        "device_id": "sensor1",
        "location": "North"
    },
    {
        "device_id": "sensor2",
        "location": "South"
    },{
        "device_id": "sensor3",
        "location": "East"
    },{
        "device_id": "sensor4",
        "location": "West"
    },
    {
        "device_id": "sensor5",
        "location": "North"
    }
]


def getDataPayload():
    record_time = trunc(time.time())
    selected_device = random.choice(sensor_locations)

    print("\Device ID: {0}".format(selected_device))
    print("\nBeginning measurements: {0}".format(record_time))

    # get some random data
    nitrogen_concentration = getNitrogenMeasurement()
    fine_concentration = getParticulateMatterMeasurement()
    coarse_concentration = getParticulateMatterMeasurement()
    oxygen_concentration = getRandomValue(30, 90) # Percentage concentration
    humidity = getRandomValue(20, 80) # Percentage humidity
    temperature = getRandomValue(25, 40) # Celcius
    wind_speed = getRandomValue(10, 25) #Km / hr
    

    # create data payload
    data_payload = {
        "device_id": selected_device["device_id"],
        "location": selected_device["location"],
        "timestamp": record_time,
        "no2_concentration": str(nitrogen_concentration),
        "fine_pm_concentration": str(fine_concentration),
        "coarse_pm_concentration": str(coarse_concentration),
        "oxygen_concentration": str(oxygen_concentration),
        "humidity": str(humidity),
        "temperature": str(temperature),
        "wind_speed": str(wind_speed),
    }

    return data_payload
