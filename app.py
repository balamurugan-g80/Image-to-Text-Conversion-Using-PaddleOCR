import os

# Disable OneDNN/MKLDNN (helps avoid some Paddle errors)
os.environ["FLAGS_use_mkldnn"] = "0"

from paddleocr import PaddleOCR

print("=" * 60)
print("IMAGE TO TEXT CONVERSION USING PADDLEOCR")
print("=" * 60)

# Initialize OCR
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en'
)

# Image file
image_path = r"C:\Users\Admin\Desktop\image to text conversion\images1.png"
try:
    print("\nReading Image:", image_path)
    print("Processing OCR...\n")

    result = ocr.ocr(image_path, cls=True)

    extracted_text = ""

    print("=" * 60)
    print("EXTRACTED TEXT")
    print("=" * 60)

    for line in result:
        for word in line:

            text = word[1][0]
            confidence = word[1][1]

            print("Text       :", text)
            print("Confidence :", round(confidence, 2))
            print("-" * 40)

            extracted_text += text + "\n"

    # Save text to file
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print("\nText saved to output.txt")

except Exception as e:
    print("\nError:", e)

print("\nProgram Finished")