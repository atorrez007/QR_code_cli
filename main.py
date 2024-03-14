import qrcode


# I need to find a way to continue looping main while maintaining state in the program until exit is called.
images = []

# Code to keep png files in order

count = 0


def add_count(count):
    print(count)
    return count


def ask_for_input(user_input):
    # Give user option to exit program
    if user_input == "exit":
        exit()

    else:
        user_input.lower()
        generate_qr(user_input)
        # add_count(count)


# generate qr code and save in file
def generate_qr(string):
    img = qrcode.make(string)
    images.append(img)
    img.save(f"user_qr_code_{add_count(count)}.png")
    print("Your QR code has been generated!")


def main():
    user_string = input(
        "Please enter a string to generate a QR code or type exit to leave program: "
    )
    ask_for_input(user_string)
    user_string.lower()


if __name__ == "__main__":
    while True:
        main()
        new_command = input(
            "Type Yes to create another QR Code or No to exit the program: "
        )
        if new_command.lower() != "yes":
            break
