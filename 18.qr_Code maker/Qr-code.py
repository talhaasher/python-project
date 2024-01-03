# The above class is a QR code generator that takes a user-provided link and generates a QR code
# image.
import image as im , qrcode 


class Generator:
    def __init__(self, link):
        self.link = link

    def qrcode_gen(self):
        gen = qrcode.QRCode(
            version=15,  # Adjust version as needed
            box_size=10,
            border=5
        )
        gen.add_data(self.link)
        gen.make(fit=True)
        img = gen.make_image(fill='black', back_color='white')
        img.save('code.png')
        return img



# The code block `if __name__ == "__main__":` is a common Python idiom that allows a module to be run
# as a standalone script.

if __name__ == "__main__":
    while True:
        user_link = input('link: ')
        generator = Generator(user_link)
        generator.qrcode_gen()
