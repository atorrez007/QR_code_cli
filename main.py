import qrcode
from random import randint


def generate_qr(string):
    img = qrcode.make(string)
    img.save(f"user_qr_code_{randint(1, 100)}.png")


def main():
    user_string = input("Please enter a string to generate a QR code: ")
    generate_qr(user_string)
    print("QR Code Generated!")


if __name__ == "__main__":
    while True:
        main()
        new_command = input(
            "Type Yes to create another QR Code or No to exit the program: "
        )
        if new_command.lower() != "yes":
            break
