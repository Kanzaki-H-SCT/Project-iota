# -*- coding: utf-8 -*-
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType, E2EEKeyChain
from .server import Server
from .session import Session
from .callback import Callback
from akad.ttypes import *
from akad.SecondaryQrCodeLoginService import Client as LoginClient
from akad.SecondaryQrCodeLoginPermitNoticeService import Client as CertClient
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
import rsa, os, base64
import urllib.parse
from urllib.parse import quote, unquote, urlencode

class Auth(object):
    isLogin     = False
    authToken   = ""
    certificate = ""

    def __init__(self):
        self.server = Server(self.appType)
        self.callback = Callback(self.__defaultCallback)
        self.server.setHeadersWithDict({
            'User-Agent': self.server.USER_AGENT,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-Carrier': self.server.CARRIER,
            'origin':'chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc'
        })

    def __loadSession(self):         
        self.talk       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_API_QUERY_PATH_FIR).Talk()
        self.poll       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_POLL_QUERY_PATH_FIR).Talk()
        self.call       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_CALL_QUERY_PATH).Call()
        self.channel    = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_CHAN_QUERY_PATH).Channel()
        self.square     = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_SQUARE_QUERY_PATH).Square()
        self.liff       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_LIFF_QUERY_PATH).Liff()
        self.shop       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_SHOP_QUERY_PATH).Shop()

        self.revision = self.poll.getLastOpRevision()
        self.isLogin = True

    def __loginRequest(self, type, data):
        lReq = LoginRequest()
        if type == '0':
            lReq.type = LoginType.ID_CREDENTIAL
            lReq.identityProvider = data['identityProvider']
            lReq.identifier = data['identifier']
            lReq.password = data['password']
            lReq.keepLoggedIn = data['keepLoggedIn']
            lReq.accessLocation = data['accessLocation']
            lReq.systemName = data['systemName']
            lReq.certificate = data['certificate']
            lReq.e2eeVersion = data['e2eeVersion']
        elif type == '1':
            lReq.type = LoginType.QRCODE
            lReq.keepLoggedIn = data['keepLoggedIn']
            if 'identityProvider' in data:
                lReq.identityProvider = data['identityProvider']
            if 'accessLocation' in data:
                lReq.accessLocation = data['accessLocation']
            if 'systemName' in data:
                lReq.systemName = data['systemName']
            lReq.verifier = data['verifier']
            lReq.e2eeVersion = data['e2eeVersion']
        else:
            lReq=False
        return lReq

    def loginWithCredential(self, _id, passwd):
        if self.systemName is None:
            self.systemName=self.server.SYSTEM_NAME
        if self.server.EMAIL_REGEX.match(_id):
            self.provider = IdentityProvider.LINE       # LINE
        else:
            self.provider = IdentityProvider.NAVER_KR   # NAVER

        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeaders('X-Line-Application', self.appName)
        self.tauth = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_AUTH_QUERY_PATH).Talk(isopen=False)

        rsaKey = self.tauth.getRSAKeyInfo(self.provider)

        message = (chr(len(rsaKey.sessionKey)) + rsaKey.sessionKey +
                   chr(len(_id)) + _id +
                   chr(len(passwd)) + passwd).encode('utf-8')
        pub_key = rsa.PublicKey(int(rsaKey.nvalue, 16), int(rsaKey.evalue, 16))
        crypto = rsa.encrypt(message, pub_key).hex()

        try:
            with open(_id + '.crt', 'r') as f:
                self.certificate = f.read()
        except:
            if self.certificate is not None:
                if os.path.exists(self.certificate):
                    with open(self.certificate, 'r') as f:
                        self.certificate = f.read()

        self.auth = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)

        lReq = self.__loginRequest('0', {
            'identityProvider': self.provider,
            'identifier': rsaKey.keynm,
            'password': crypto,
            'keepLoggedIn': self.keepLoggedIn,
            'accessLocation': self.server.IP_ADDR,
            'systemName': self.systemName,
            'certificate': self.certificate,
            'e2eeVersion': 0
        })

        result = self.auth.loginZ(lReq)

        if result.type == LoginResultType.REQUIRE_DEVICE_CONFIRM:
            self.callback.PinVerified(result.pinCode)

            self.server.setHeaders('X-Line-Access', result.verifier)
            getAccessKey = self.server.getJson(self.server.parseUrl(self.server.LINE_CERTIFICATE_PATH), allowHeader=True)

            self.auth = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)

            try:
                lReq = self.__loginRequest('1', {
                    'keepLoggedIn': self.keepLoggedIn,
                    'verifier': getAccessKey['result']['verifier'],
                    'e2eeVersion': 0
                })
                result = self.auth.loginZ(lReq)
            except:
                raise Exception('Login failed')

            if result.type == LoginResultType.SUCCESS:
                if result.certificate is not None:
                    with open(_id + '.crt', 'w') as f:
                        f.write(result.certificate)
                    self.certificate = result.certificate
                if result.authToken is not None:
                    self.loginWithAuthToken(result.authToken)
                else:
                    return False
            else:
                raise Exception('Login failed')

        elif result.type == LoginResultType.REQUIRE_QRCODE:
            self.loginWithQrCode()
            pass

        elif result.type == LoginResultType.SUCCESS:
            self.certificate = result.certificate
            self.loginWithAuthToken(result.authToken)

    def loginWithQrCode(self, cert=""):
        if self.systemName is None:
            self.systemName=self.server.SYSTEM_NAME
        if self.appName is None:
            self.appName=self.server.APP_NAME        
        headers = {
            "X-Line-Application": self.appName,
            "User-Agent": self.systemName,
        }        
        http_client = THttpClient.THttpClient(self.server.LINE_QRCODE_LOGIN_PATH)
        http_client.setCustomHeaders(headers)
        protocol = TCompactProtocol.TCompactProtocol(http_client)
        client = LoginClient(iprot=protocol)
        http_client.open()
        session_id = client.createSession(CreateQrSessionRequest()).authSessionId
        p_key = self.generateKeypair()
        #print(p_key)
        secret = base64.b64encode(p_key.public_key).decode()
        #secret_query = create_secret_query(p_key.public_key)
        #secret_query = self.generateParams()
        #print(secret_query)
        self.callback.QrUrl(client.createQrCode(CreateQrCodeRequest(session_id)).callbackUrl+'?secret={secret}&e2eeVersion=1'.format(secret=quote(secret)))
        #self.callback.QrUrl(client.createQrCode(LoginQrCode_CreateQrCodeRequest(session_id)).callbackUrl + '?secret=' +secret_query+'&e2eeVersion=1')
        headers = {
            "User-Agent": self.systemName,
            "X-Line-Application": self.appName,
            "X-Lal": "en_us",
            "X-Line-Access": session_id
        }
        http_client = THttpClient.THttpClient(self.server.LINE_PERMIT_NOTICE_PATH)
        http_client.setCustomHeaders(headers)
        protocol = TCompactProtocol.TCompactProtocol(http_client)
        auth = CertClient(iprot=protocol)
        http_client.open()
        auth.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session_id))
        try:
            client.verifyCertificate(VerifyCertificateRequest(session_id, cert))
        except:
            print(client.createPinCode(CreatePinCodeRequest(session_id)))
            auth.checkPinCodeVerified(CheckPinCodeVerifiedRequest(session_id))
        result = client.qrCodeLogin(QrCodeLoginRequest(session_id, self.server.SYSTEM_NAME, False))
        self.loginWithAuthToken(result.accessToken)
        self.certificate = result.certificate

    def loginWithAuthToken(self, authToken=None):
        if authToken is None:
            raise Exception('Please provide Auth Token')
        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeadersWithDict({
            'X-Line-Application': self.appName,
            'X-Line-Access': authToken
        })
        self.authToken = authToken
        self.__loadSession()

    def __defaultCallback(self, str):
        print(str)

    def logout(self):
        self.isLogin = False
        self.auth.logoutZ()
