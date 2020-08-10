# by Richi Rod AKA @richionline / falken20


from requests import Session


class ResponseException(Exception):
    pass


class LoginException(Exception):
    pass


class SessionException(Exception):
    pass


class NoResponseException(Exception):
    pass


class SelectContractException(Exception):
    pass


class Energy:

    _domain = "https://www.i-de.es/consumidores/rest"
    _login_url = _domain + "/loginNew/login"
    _reading_url = _domain + "/escenarioNew/obtenerMedicionOnline/12"
    _reading_of_the_day_url = _domain + "/consumoNew/obtenerDatosConsumo/fechaInicio" \
                                        "/{date}/colectivo/USU/frecuencia/horas/acumular/false"
    _icp_status_url = _domain + "/rearmeICP/consultarEstado"
    _contracts_url = _domain + "/cto/listaCtos/"
    _contract_detail_url = _domain + "/detalleCto/detalle/"
    _contract_selection_url = _domain + "/cto/seleccion/"
    _obtener_escenarios_url = _domain + "/escenarioNew/obtenerEscenariosRest/"
    _obtener_escenarios_contador_url = _domain + "/escenarioNew/obtenerEscenariosRestContador/"

    _headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
                      "Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36",
        'accept': "application/json; charset=utf-8",
        'content-type': "application/json; charset=utf-8",
        'cache-control': "no-cache"
    }

    def __init__(self, user, password):
        """Energy class __init__ method"""
        self._user = user
        self._password = password
        self._token = None
        self._cookie = None
        self._session = None

    def login(self):
        """Creates session with your credentials"""
        self._session = Session()
        login_data = "[\"{}\",\"{}\",null,\"Linux -\",\"PC\",\"Chrome 77.0.3865.90\",\"0\",\"\",\"s\"]".format(self._user, self._password)
        response = self._session.request("POST", self._login_url, data=login_data, headers=self._headers)
        if response.status_code != 200:
            self._session = None
            raise ResponseException("Response error, code: {}".format(response.status_code))
        json_response = response.json()
        if json_response["success"] != "true":
            self._session = None
            raise LoginException("Login error, bad login")

    def _check_session(self):
        if not self._session:
            raise SessionException("Session required, use login() method to obtain a session")

    def reading(self):
        """Returns your current power consumption."""
        self._check_session()
        response = self._session.request("GET", self._reading_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException(response)
        if not response.text:
            raise NoResponseException(response)
        json_response = response.json()
        # return json_response['valMagnitud']
        return json_response

    def reading_of_the_day(self):
        """Returns your current power consumption."""
        self._check_session()
        response = self._session.request("GET", self._reading_of_the_day_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return json_response

    def icp_status(self):
        """Returns the status of your ICP."""
        self._check_session()
        response = self._session.request("POST", self._icp_status_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        print(json_response)
        if json_response["icp"] == "true":
            return True
        else:
            return False

    def contracts(self):
        self._check_session()
        response = self._session.request("GET", self._contracts_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        if json_response["success"]:
            return json_response["contratos"]

    def contract(self):
        self._check_session()
        response = self._session.request("GET", self._contract_detail_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        return response.json()

    def contractselect(self, id):
        self._check_session()
        response = self._session.request("GET", self._contract_selection_url + id, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        if not json_response["success"]:
            raise

    def escenarios(self):
        self._check_session()
        response = self._session.request("GET", self._obtener_escenarios_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return json_response

    def escenarios_contador(self):
        self._check_session()
        response = self._session.request("POST", self._obtener_escenarios_contador_url, headers=self._headers)
        if response.status_code != 200:
            raise ResponseException
        if not response.text:
            raise NoResponseException
        json_response = response.json()
        return json_response
