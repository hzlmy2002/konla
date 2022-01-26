"""
PDF text extracter using OCR (Optical Character Recognition)

References:
PDF to images: https://stdworkflow.com/272/say-goodbye-to-copy-paste-python-implements-pdf-to-text
Pytesseract OCR: https://nanonets.com/blog/ocr-with-tesseract/

Convert each page of a PDF to a PNG. Then use OCR to convert to text
"""
from pdf2image import convert_from_path
import pytesseract
import os


def save_images(images, images_dir):
    """ Save images into directory """
    # Empty the image directory before storing new PDF images
    for f in os.listdir(images_dir):
        os.remove(os.path.join(images_dir, f))

    # Store each image
    for i, img in enumerate(images):
        # Save pages as images in the PDF
        img.save(f"{images_dir}/{i}.png", 'PNG')


def get_image_filenames(image_files):
    """ Get files from directory and sort them by integer """
    # Split filename by '.' to get filename integer
    image_files_split = [i.split(".") for i in image_files]

    # Convert to filename to integer
    image_files_int = [[int(i[0]), i[1]] for i in image_files_split]

    # Sort filename integers
    image_files_int.sort()

    # Join together filename and png extension
    image_files = [f"{i[0]}.{i[1]}" for i in image_files_int]

    return image_files


def extract_text(images_dir):
    """ Extract text from image using OCR """
    content = ""

    image_files = get_image_filenames(os.listdir(images_dir))

    for img_filename in image_files:
        print(f"Processing {img_filename}...")
        # Process each image file to extract the text
        content += pytesseract.image_to_string(f"{images_dir}/{img_filename}")

    return content


def save_content(content):
    """ Save content to output file """
    with open("pdf_text_output.txt", "wb") as f:
        content_split = content.split("\n")
        for line in content_split:
            # Check line has content
            if len(line) > 0:
                try:
                    encoded_line = (line + '\n').encode("utf8")
                    f.write(encoded_line)
                except:
                    pass


pdf_filename = "../../shapes.pdf"
images_dir = "pdf_images"

# Get images of PDF pages
images = convert_from_path(pdf_filename)

# Save the images
#save_images(images, images_dir)

# Extract text using OCR
content = extract_text(images_dir)

# Save content from extraction
save_content(content)
