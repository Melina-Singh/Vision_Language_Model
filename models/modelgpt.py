from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptioningModel:
    def __init__(self):
        # Initialize BLIP model and processor
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def generate_caption(self, image):
        # Make sure the input is a PIL Image object
        if isinstance(image, Image.Image):
            # Preprocess the image and generate the caption
            inputs = self.processor(images=image, return_tensors="pt")

            # Use the model to generate a caption
            out = self.model.generate(**inputs)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            return caption
        else:
            raise ValueError("Expected a PIL Image object.")
