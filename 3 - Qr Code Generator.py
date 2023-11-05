import qrcode
import os

qr_klasoru = "Qr Kodlarım"
os.makedirs(qr_klasoru, exist_ok=True)

input_URL = input("URL'yi girin: ")

if not input_URL:
    print("Hata: URL girmediniz.")
else:
    sayac = 0

    while True:
        dosya_adi = (f"{qr_klasoru}/url_qrcode_{sayac}.png")

        if not os.path.exists(dosya_adi):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=15,
                border=4,
            )

            qr.add_data(input_URL)
            qr.make(fit=True)

            resim = qr.make_image(fill_color="black", back_color="white")
            resim.save(dosya_adi)

            print(f"QR kod dosyasına kaydedildi: {dosya_adi}")
            break
        else:
            sayac += 1
