# by Richi Rod AKA @richionline / falken20

from src import __version__
from src.utils import JSONUtils
from src.energy import Energy
import logging


def get_auth_info_energy():
    """
    Request for user and password variables to be able to login in energy company
    """
    try:
        user = 'ricardorg20@gmail.com'  # os.environ["IBUSER"]
        password = 'bXWkbuvnGF2YdsphK'  # os.environ["IBPASS"]
    except KeyError:
        print("You must to configure `IBUSER` and `IBPASS` to continue")
        sys.exit(-1)
    return user, password


def get_energy_data():
    auth = get_auth_info_energy()
    energy = Energy(*auth)
    energy.login()
    print('**************** Data Contract')
    JSONUtils.pprint(energy.contract())
    print('**************** Current Power Consumption')
    JSONUtils.pprint(energy.watt_hour_meter())

def main():
    print('**************** HOUSE DATA SYSTEM by @richionline')
    print('**************** %s' % __version__)

    logging.info('ROD -----> Getting data for energy company')
    get_energy_data()

    print('**************** 2020 by @richionline')


if __name__ == '__main__':
    main()
