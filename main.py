import qrcode
from random import randint


def generate_qr(user_string, preference):
    if preference.lower().strip() == "h":
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
    qr.add_data(user_string)
    qr.make(fit=True)
    img = qr.make_image(fill_color=f"{fill_choice}", back_color=f"{back_choice}")
    img.save(f"user_qr_code_{randint(1, 100)}.png")


def main():
    user_string = input("Please enter the data you want to encode: ")
    user_style = input(
        "Are you a hacker or a civilian? Type 'H' for Hacker and 'C' for Civilian: "
    )
    generate_qr(user_string, user_style)
    print("QR Code Generated!")


if __name__ == "__main__":
    while True:
        main()
        new_command = input(
            "Do you want to generate a new QR Code? Type 'Y' for Yes and 'N' to Exit the Program: "
        )
        if new_command.lower().strip() != "y":
            break
