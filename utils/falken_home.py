# by Richi Rod AKA @richionline / falken20
import os
import sys
from dotenv import load_dotenv
import logging

# Go to the parent folder for importing other project files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app_home.utils import JSONUtils
from utils.energy import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Looking for .env file for environment vars
load_dotenv(os.path.join(BASE_DIR, '.env'), override=True)

# Set the format of logging messages
logging.basicConfig(format=f'{os.getenv("ID_LOG", "")} %(levelname)s:%(asctime)s: '
                           f'File: %(filename)s: Function: %(funcName)s\n'
                           '%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=os.getenv("DJANGO_LOG_LEVEL", ""))


def get_auth_info_energy():
    """
    Request for user and password variables to be able to login in energy company
    """
    try:
        user = os.environ["ENERGY_USER"]
        password = os.environ["ENERGY_PASS"]
    except KeyError:
        print("You must to configure environment vars `ENERGY_USER` and `ENERGY_PASS` to continue")
        sys.exit(-1)
    return user, password


def get_energy_data():
    auth = get_auth_info_energy()
    energy = Energy(*auth)
    try:
        energy.login()
        print('**************** Data Contract')
        JSONUtils.pprint(energy.contract())
        print('**************** Data ICP status')
        # JSONUtils.pprint(energy.icp_status())
        print('**************** Current Power consumption')
        # JSONUtils.pprint(energy.reading())
        print('**************** Scenarios')
        JSONUtils.pprint(energy.escenarios())
        print('**************** Scenarios Counter')
        JSONUtils.pprint(energy.escenarios_contador())
    except Exception as err:
        logging.error(f'Line: {err.__traceback__.tb_lineno} \n'
                      f'Type: {type(err).__name__} \n'
                      f'Arguments:\n {err.args}')


def main():
    print('**************** HOUSE DATA SYSTEM by @richionline')
    print('**************** Getting data for energy company')
    get_energy_data()
    print('**************** 2020 by @richionline')


if __name__ == '__main__':
    main()
