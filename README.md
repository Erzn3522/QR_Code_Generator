# QR Code Generator


![GIF](https://64.media.tumblr.com/tumblr_m32e3dxGr71qg6rkio1_r1_500.gifv)

This project is a simple QR code generator that creates QR codes for Wi-Fi networks and passwords. It provides functionality to generate QR codes for Wi-Fi network credentials and copy the password to the clipboard.

## Usage

### Requirements

- Python 3.x
- qrcode library
- pyperclip library

### Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:

``` pip install qrcode pyperclip ```

### Project Structure

- `main.py`: The main entry point of the project. It creates instances of `FolderController`, `WifiQrCodeCreator`, and `PasswordQrCodeCreator` to generate the QR codes.
- `FolderController.py`: Contains the `FolderController` class, responsible for creating and managing the images folder where the QR codes will be saved.
- `QrCodeCreator.py`: Contains the `QrCodeCreatorBase` class as the base class for QR code creation, and the `WifiQrCodeCreator` and `PasswordQrCodeCreator` classes for generating Wi-Fi and password QR codes, respectively.

### Running the Project

1. Open a terminal and navigate to the project directory.
2. Run the following command to execute the project:


The QR codes for the Wi-Fi network and password will be generated and saved in the `images` folder within the project directory. The password will also be copied to the clipboard.

## Customization

You can customize the Wi-Fi network name and password by modifying the `ssid` and `password` variables in the `main.py` file.

## License

This project is licensed under the [MIT License](LICENSE).

