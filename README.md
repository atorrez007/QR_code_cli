# QR Code Generator for Python - CLI

This is a command-line interface (CLI) QR code generator written in Python. This tool allows you to quickly generate QR codes with custom styling options.

## Features
- Generate QR codes from user input strings.
- Customize QR code appearance based on user preference.
- Support for generating multiple QR codes in a session.

## Sample Codes
<div style="display:flex;">
    <img src="https://github.com/atorrez007/QR_code_cli/blob/main/user_qr_code_93.png" alt="Alt text 1" width="300" >
    <img src="https://github.com/atorrez007/QR_code_cli/blob/main/user_qr_code_71.png" alt="Alt text 2" width="300" >
</div>

## Installation
To use this CLI QR code generator, make sure you have Python installed on your system. Additionally, you need to install the `qrcode` library.

You can install the required library using pip:




```pip install qrcode```


To generate a QR code, simply run the script main.py:



```python main.py```

## Follow the on-screen instructions:

Please enter the data you want to encode:

Choose your styling preference: "hacker" or "civilian".

Once the QR code is generated, it will be saved in the current directory.

You can generate multiple QR codes in one session. After each generation, you'll be prompted whether you want to create another QR code.

Customization
You can customize the QR code appearance by choosing between "hacker" or "civilian" styles. The "hacker" style uses green fill and black background, while the "civilian" style uses black fill and white background.

## Example
Here's a basic example of how to use the QR code generator:


```
python main.py
Please enter the data you want to encode: www.github.com/atorrez007
Are you a hacker or a civilian? hacker

QR Code Generated!

Do you want to generate a new QR Code? Type 'Y' for Yes and 'N' to Exit the Program: N
```
License
This project is licensed under the MIT License - see the LICENSE file for details.
