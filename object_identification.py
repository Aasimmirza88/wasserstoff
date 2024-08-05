from transformers import CLIPProcessor, CLIPModel

# pre-trained CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Function to identify objects
def identify_objects(object_paths):
    descriptions = {}
    for object_id, object_path in object_paths.items():
        image = Image.open(object_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)
        
        description = "Label not found" 
        descriptions[object_id] = description
    
    return descriptions


object_paths = {object_id: row[3] for object_id, row in c.execute("SELECT * FROM objects").fetchall()}
descriptions = identify_objects(object_paths)
