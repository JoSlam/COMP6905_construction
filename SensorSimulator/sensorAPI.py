from random import randint, uniform
import enum

precision = 2

class ParticulateMatterType(enum.Enum):
    Fine = 1
    Coarse = 2

# measured in parts per billion
# sample data will consider the Efento wireless NO2 sensor (0-4 or 4000 ppb)
def getNitrogenMeasurement():
    min = 50
    max = 300s
    return round(uniform(min, max), precision)


def getParticulateMatterMeasurement(pmType):
    min = randint(10, 50)
    max = randint(min, 350)
    
    if(pmType == repr(ParticulateMatterType.Fine)):
        return getFineMeasurement(min, max)
    else:
        return getCoarseMeasurement(min, max)


def getFineMeasurement(min, max):
    return round(uniform(min, max), precision)

def getCoarseMeasurement(min, max):
    return round(uniform(min, max), precision)

