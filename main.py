import qrcode


# I need to find a way to continue looping main while maintaining state in the program until exit is called.

# When the QR code is generated, the img is appended to the images list.
images = []

count = 0


def add_count(count):
    print(f"Previous count is {count}")

    return count + 1


# generate qr code and save in file
def generate_qr(string):
    img = qrcode.make(string)
    images.append(img)
    img.save(f"user_qr_code_{count + 1}.png")
    print("Your QR code has been generated!")


def main():
    user_string = input("Please enter a string to generate a QR code: ")
    generate_qr(user_string)


if __name__ == "__main__":
    while True:
        main()
        new_command = input(
            "Type Yes to create another QR Code or No to exit the program: "
        )
        if new_command.lower() != "yes":
            break
