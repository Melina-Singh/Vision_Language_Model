import streamlit as st
from models.visiontr import ResNetModel
from models.modelgpt import ImageCaptioningModel
from utils.image_utils import load_image, resize_image
from utils.text_utils import format_caption


classification_model = ResNetModel()
captioning_model = ImageCaptioningModel()

# Streamlit app UI
st.title("Image Classification and Captioning App")
st.write("Upload two images at once to classify and generate descriptions.")

# Upload two images
uploaded_images = st.file_uploader("Choose two images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if len(uploaded_images) == 2:
    # Process the first image
    image1 = load_image(uploaded_images[0])
    image1 = resize_image(image1)  # Resize the image for better display

    # Process the second image
    image2 = load_image(uploaded_images[1])
    image2 = resize_image(image2)  # Resize the image for better display

    # Create columns to display the images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Image 1")
        st.image(image1, caption="Uploaded Image 1", use_container_width=True)

        # Classify the first image
        classification_result1 = classification_model.classify_image(image1)
        st.write(f"Predicted Class for Image 1: {classification_result1}")

        # Generate caption for the first image
        caption1 = captioning_model.generate_caption(image1)
        formatted_caption1 = format_caption(caption1)  # Format the caption
        st.write(f"Generated Caption : {formatted_caption1}")

    with col2:
        st.subheader("Image 2")
        st.image(image2, caption="Uploaded Image 2", use_container_width=True)

        # Classify the second image
        classification_result2 = classification_model.classify_image(image2)
        st.write(f"Predicted Class for Image 2: {classification_result2}")

        # Generate caption for the second image
        caption2 = captioning_model.generate_caption(image2)
        formatted_caption2 = format_caption(caption2)  # Format the caption
        st.write(f"Generated Caption : {formatted_caption2}")
else:
    st.warning("Please upload exactly two images to proceed.")
