from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptioningModel:
    def __init__(self):
        """
        Initializes the BLIP model for image captioning. 
        The BLIP (Bootstrapping Language-Image Pretraining) model is a powerful model 
        used for generating natural language descriptions from images.
        
        The constructor loads the BLIP processor and model weights from the Salesforce 
        pre-trained repository to facilitate image caption generation.

        Attributes:
            processor (BlipProcessor): Preprocessing utility for images and text used by BLIP.
            model (BlipForConditionalGeneration): The BLIP model for generating captions from images.
        """
        # Load the BLIP processor and model from the pre-trained Salesforce repository
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        
        # Check if the model and processor are successfully loaded
        print("BLIP model and processor initialized successfully.")

    def generate_caption(self, image):
        """
        Generates a caption for a given image using the BLIP model.
        
        This method takes an image, processes it using the BLIP processor, and then 
        generates a caption using the BLIP model. The caption is returned as a string..
        Args:
            image (PIL.Image.Image): A PIL Image object that represents the input image to be captioned.
        Returns:
            str: A generated caption describing the image.
        Raises:
            ValueError: If the input image is not a PIL Image object.
        """
        
        # Ensure the input is a PIL Image object
        if not isinstance(image, Image.Image):
            raise ValueError("Expected a PIL Image object. Please provide a valid image.")

        
        print("Preprocessing image for caption generation...")
        # Preprocess
        inputs = self.processor(images=image, return_tensors="pt")
        
        # Log the shape of the input tensor for debugging purposes
        print(f"Input tensor shape: {inputs['pixel_values'].shape}")

        # Use the BLIP model to generate the caption (in the form of token IDs)
        print("Generating caption using BLIP model...")
        with torch.no_grad():
            out = self.model.generate(**inputs)

        # Decode the generated tokens into a human-readable caption
        caption = self.processor.decode(out[0], skip_special_tokens=True)

        print(f"Generated Caption: {caption}")
        return caption
