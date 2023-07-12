import qrcode
import pyperclip
import os

class QrCodeCreatorBase:
    def _create_qr_code(self, data, filename):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(filename)

class WifiQrCodeCreator(QrCodeCreatorBase):
    def create_wifi_qr_code(self, ssid, password, path):
        wifi_data = f"WIFI:S:{ssid};T:WPA;P:{password};;"
        qr_filename = "wifi_qr_code.png"
        filename  = os.path.join(path, qr_filename)
        self._create_qr_code(wifi_data, filename)

class PasswordQrCodeCreator(QrCodeCreatorBase):
    def create_password_qr_code(self, password, path):
        qr_filename = "password_qr_code.png"
        filename = os.path.join(path, qr_filename)
        self._create_qr_code(password, filename)
        pyperclip.copy(password)
        print("Password copied to clipboard.")

