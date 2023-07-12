from FolderController import FolderController
from QrCodeCreator import WifiQrCodeCreator, PasswordQrCodeCreator

if __name__ == '__main__':
    folder_controller = FolderController()
    folder_controller.create_images_folder()
    image_path = folder_controller.get_images_path()

    ssid = "wiif_network_name"
    password = "wifi_password"

    wifi_qr_generator = WifiQrCodeCreator()
    password_qr_generator = PasswordQrCodeCreator()

    wifi_qr_generator.create_wifi_qr_code(ssid, password, image_path)
    password_qr_generator.create_password_qr_code(password, image_path)
