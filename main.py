import cv2
import pytesseract
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from typing import Tuple, List

class App:
    def __init__(self) -> None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.font: ImageFont.FreeTypeFont = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 24)

    def to_text(self, path: str, out: str) -> None:
        self.img: np.ndarray = cv2.imread(path)
        self.gray: np.ndarray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.gray: np.ndarray = cv2.resize(self.gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        _, self.binary = cv2.threshold(self.gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        self.text: str = pytesseract.image_to_string(self.binary, lang='rus+eng')
        
        lines: List[str] = self.text.split('\n')
        max_width: int = 0
        for line in lines:
            bbox: Tuple[int, int, int, int] = self.font.getbbox(line)
            max_width = max(max_width, bbox[2] - bbox[0])
        
        height: int = len(lines) * 30 + 40
        width: int = max(max_width + 40, self.img.shape[1])
        
        self.result: Image.Image = Image.new('RGB', (width, height), (0, 0, 0))
        self.draw: ImageDraw.Draw = ImageDraw.Draw(self.result)

        y: int = 20
        for line in lines:
            self.draw.text((20, y), line, fill=(255, 255, 255), font=self.font)
            y += 30
        
        self.result.save(out)
        print(self.text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Пример: python main.py {путь изображения} {куда сохранять}")
        sys.exit(1)
    
    path: str = sys.argv[1]
    out: str = sys.argv[2]
    app: App = App()
    app.to_text(path, out)