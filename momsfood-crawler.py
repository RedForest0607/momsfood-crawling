from PIL import Image
import os
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
config = ('-l kor --oem 3 --psm 11')

# https://blog.naver.com/momsfood_ 맘스푸드 블로그 주소

def main(argv):
    for filename in os.listdir("."):
        if str(filename) not in ['.','..']:
            nameParts = str(filename).split(".")
        if nameParts[-1].lower() in ["gif", "png", "jpg", "jpeg"]:
            try:
                print("Found file " + str(filename))
                ocrText = pytesseract.image_to_string(str(filename), timeout=5, config=config)
                print (ocrText)
                print("")
            except Exception as err:
                print("error occured" + err.with_traceback(tb))
if __name__ == "__main__":
    main(sys.argv[1:])