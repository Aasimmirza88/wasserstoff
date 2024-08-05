import torch
import torchvision
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

#A pre-trained Mask R-CNN model
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Function to perform segmentation
def segment_image(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
    image_tensor = transform(image)
    with torch.no_grad():
        predictions = model([image_tensor])[0]

    # Extract masks, boxes, and labels
    masks = predictions['masks'].numpy()
    boxes = predictions['boxes'].numpy()
    labels = predictions['labels'].numpy()

    #Segmented objects
    for i in range(masks.shape[0]):
        mask = masks[i, 0]
        masked_image = np.array(image)
        masked_image[mask == 0] = 0
        plt.figure()
        plt.imshow(masked_image)
        plt.title(f'Object {i + 1} (Label: {labels[i]})')
        plt.show()

# Example usage
segment_image('input_image.jpg')
