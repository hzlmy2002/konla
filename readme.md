# Code Repository
## Tika Installation
Installation process for text extraction using Tika
```bash
pip install tika
```
### Note:
Tika is written in Java, so you need a java runtime installed

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

## pdftotext installation
### 1.
Dependencies that allow pdftotext to work
```bash
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

### 2.
```bash
pip install pdftotext
```
