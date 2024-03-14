import qrcode
from random import randint


def generate_qr(string, preference):
    if preference.lower() == "hacker":
        fill_choice = "green"
        back_choice = "black"
    else:
        fill_choice = "black"
        back_choice = "white"

    # customization of qrcode class
    qr = qrcode.QRCode(
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=8,
    )
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image(fill_color=f"{fill_choice}", back_color=f"{back_choice}")
    img.save(f"user_qr_code_{randint(1, 100)}.png")


def main():
    user_string = input("Please enter a string to generate a QR code: ")
    user_style = input("Are you a hacker or a civilian? ")
    generate_qr(user_string, user_style)
    print("QR Code Generated!")


if __name__ == "__main__":
    while True:
        main()
        new_command = input(
            "Type Yes to create another QR Code or No to exit the program: "
        )
        if new_command.lower() != "yes":
            break
