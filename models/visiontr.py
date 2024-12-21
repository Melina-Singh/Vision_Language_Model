# vision_model.py

from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch

class ResNetModel:
    def __init__(self, model_name="microsoft/resnet-50"):
        # Load ResNet model and feature extractor
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
        self.model = AutoModelForImageClassification.from_pretrained(model_name)

    def classify_image(self, image):
        '''Classifies an input image and returns the predicted label using the 
        pre-trained ResNet model. The image is processed and passed through 
        the model to generate the classification result.
        Args:
            image (PIL.Image.Image): The input image to be classified.
        Returns:
            str: The predicted label for the input image based on the classification model.'''
        
        # Preprocess the image
        inputs = self.feature_extractor(images=image, return_tensors="pt")

        # Run inference
        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_label = self.model.config.id2label[predicted_class_idx]

        return predicted_label
