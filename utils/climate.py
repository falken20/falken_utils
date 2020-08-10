
"""
API Daikin: https://github.com/ael-code/daikin-control
"""

import requests
from time import sleep
import logging
import os

AIR_CONDITIONERS = {u'Salón': 'ip.ip.ip.ip', 'Other Room': 'ip.ip.ip.ip'}


def read_temp():
    """ Calls sensor information """
    for machine in AIR_CONDITIONERS:
        print("ROD: Establish connection with %s and url http://%s/aircon/get_sensor_info" % (machine, AIR_CONDITIONERS[machine]))
        r = requests.get(url="http://%s/aircon/get_sensor_info" % AIR_CONDITIONERS[machine])
        response = r.text
        parameters = response.split(',')
        for parameter in parameters:
            if parameter.startswith("htemp"):
                inside = float(parameter.split("=")[1])
            if parameter.startswith("otemp"):
                outside = float(parameter.split("=")[1])
        print (u"%s: %dºC %dºC" % (machine, inside, outside))


# Detail doc of "__name__ == __main__" use: https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main
if __name__ == '__main__':
    while True:
        read_temp()
        sleep(60)
