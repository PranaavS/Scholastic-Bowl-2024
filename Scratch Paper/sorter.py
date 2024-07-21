from pyzbar.pyzbar import decode
from PIL import Image
from pdf2image import convert_from_path
import os

if __name__ == "__main__":
    for filename in os.listdir("Scratch Paper/USED"):
        # Open the image file
        src_path = f"Scratch Paper/USED/{filename}"
        image_list = convert_from_path(src_path)
        document = image_list[0]

        # Decode the QR code or barcode
        data = decode(document)[0].data.decode().split("\n")

        # Set destination path
        dest_path = os.path.join(data[3], "Scratch Paper")

        try:
            os.mkdir(dest_path)
        except Exception as e:
            pass

        # Move source file to destination
        os.rename(src_path, dest_path + f"/{data[0]}.pdf")

        print(data)