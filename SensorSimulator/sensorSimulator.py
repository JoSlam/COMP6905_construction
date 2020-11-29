from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from payloadSimulator import getDataPayload
import random
import time
import json

# Automatically called whenever the shadow is updated.


def updateCallback(payload, responseStatus, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER +
          '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + responseStatus)
    print("token = " + token)


def loadConfig(file_path):
    config = {}
    with open(file_path) as config_file:
        config = json.load(config_file)
    return config


print("\nSimulator bootstrap time: {0}".format(time.time()))

client_config = loadConfig("config.json")

SHADOW_CLIENT = client_config["shadow_client"]
HOST_NAME = client_config["hostname"]
ROOT_CA = client_config["root_ca"]
PRIVATE_KEY = client_config["private_key"]
CERT_FILE = client_config["certificate"]
SHADOW_HANDLER = client_config["shadow_handler"]


# Create, configure, and connect a shadow client.
shadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
shadowClient.configureEndpoint(HOST_NAME, 8883)
shadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,
                                  CERT_FILE)
shadowClient.configureConnectDisconnectTimeout(10)
shadowClient.configureMQTTOperationTimeout(5)
shadowClient.connect()

deviceShadow = shadowClient.createShadowHandlerWithName(
    SHADOW_HANDLER, True)

while True:
    # Get random data payload
    data_payload = {
        "state": {
            "reported": getDataPayload()
        }
    }

    print("data payload: {0}".format(data_payload))
    # send device update
    deviceShadow.shadowUpdate(json.dumps(data_payload),
                              updateCallback, 5)

    # sleep thread for 10 minutes
    time.sleep(600)
