# Code Repository

## OCR installation
Installation process for OCR text extraction on Linux

### 1.
Poppler utils allows pdf2image to work
```bash
sudo apt get install poppler-utils
```

### 2.
pdf2image converts each page of a PDF into an image
```bash
pip install pdf2image
```

### 3.
Allows pytesseract to work
```bash
sudo apt install tesseract-ocr -y
```

### 4.
pytesseract performs the OCR process on an image
```bash
pip install pytesseract
```
