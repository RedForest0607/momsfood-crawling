from PIL import Image
import bs4
import os
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
config = ('--psm 4 -c tessedit_create_hocr=1')

# https://blog.naver.com/momsfood_ 맘스푸드 블로그 주소

def main(argv):
    for filename in os.listdir("."):
        if str(filename) not in ['.','..']:
            nameParts = str(filename).split(".")
        if nameParts[-1].lower() in ["gif", "png", "jpg", "jpeg"]:
            try:
                # print("Found file " + str(filename))
                # ocrText = pytesseract.image_to_string(str(filename), timeout=5, config=config)
                # print (ocrText)
                # print("")
                pytesseract.pytesseract.run_tesseract(str(filename), str(filename+"_parsed"), extension='png', lang = 'kor', config=config)
                xml_input = open(str(filename+"_parsed.hocr"), "r", encoding="utf-8")
                soup = bs4.BeautifulSoup(xml_input, 'lxml')

                ocr_lines = soup.findAll("span", {"class": "ocr_line"})

                lines_structure = []
                for line in ocr_lines:
                    line_text = line.text.replace("\n", " ").strip()
                    title = line['title']
                    x1, y1, x2, y2 = map (int, title[5:title.find(";")].split())
                    lines_structure.append({"x1":x1, "y1": y1, "x2": x2, "y2": y2, "text":line_text})
            except Exception as err:
                print("error occured" + err.with_traceback(tb))
if __name__ == "__main__":
    main(sys.argv[1:])