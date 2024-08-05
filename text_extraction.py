import pytesseract

# Function to extract text from object images
def extract_text_from_objects(object_paths):
    texts = {}
    for object_id, object_path in object_paths.items():
        image = Image.open(object_path).convert("RGB")
        text = pytesseract.image_to_string(image)
        texts[object_id] = text.strip()
    
    return texts

# Example usage
texts = extract_text_from_objects(object_paths)
