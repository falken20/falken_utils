# by Richi Rod AKA @richionline / falken20

from utils import __version__
from utils.utils import JSONUtils
from utils.energy import *
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
    try:
        energy.login()
        print('**************** Data Contract')
        JSONUtils.pprint(energy.contract())
        print('**************** Data ICP status')
        JSONUtils.pprint(energy.icp_status())
        print('**************** Current Power consumption')
        JSONUtils.pprint(energy.reading())
        print('**************** Scenarios')
        JSONUtils.pprint(energy.escenarios())
        print('**************** Scenarios Counter')
        JSONUtils.pprint(energy.escenarios_contador())
    except ResponseException as e:
        print('>>>>> ERROR ResponseException:\n %s' % e)
    except LoginException as e:
        print('>>>>> ERROR LoginException:\n %s' % e)
    except SessionException as e:
        print('>>>>> ERROR SessionException:\n %s' % e)
    except NoResponseException as e:
        print('>>>>> ERROR NoResponseException:\n %s' % e)
    except SelectContractException as e:
        print('>>>>> ERROR SelectContractException:\n %s' % e)
    except Exception as e:
        print('>>>>> ERROR Exception:\n %s' % e)


def main():
    print('**************** HOUSE DATA SYSTEM by @richionline')
    print('**************** Build: %s' % __version__)

    print('**************** Getting data for energy company')
    get_energy_data()

    print('**************** 2020 by @richionline')


if __name__ == '__main__':
    main()
