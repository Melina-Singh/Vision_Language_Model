from PIL import Image
import io

def load_image(uploaded_file):
    """
    Load an image from a file-like object (e.g., uploaded file in Streamlit).
    """
    image = Image.open(uploaded_file)
    return image

def resize_image(image, size=(400, 400)):
    """
    Resize the image to a specific size for better display.
    """
    image = image.resize(size)
    return image
