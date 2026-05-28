from app.preprocess import preprocess_image
from app.extractor import extract_text


def main():
    image_path = "assets/sample.png"

    processed_image = preprocess_image(image_path)

    extracted_text = extract_text(processed_image)

    print("\nExtracted Text:\n")
    print(extracted_text)

    with open("output/result.txt", "w") as file:
        file.write(extracted_text)


if __name__ == "__main__":
    main()