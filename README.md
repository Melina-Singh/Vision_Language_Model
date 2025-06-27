
# Image Captioning with BLIP and ResNet50

This is a simple multimodal application that generates natural language captions for images using a combination of **ResNet50** and **BLIP (Bootstrapped Language-Image Pretraining)**. The app is built and deployed using **Streamlit**, providing an interactive web interface for image captioning.


##  Project Overview

The application demonstrates how pretrained vision and language models can work together to understand visual content and describe it in text. Users can upload an image through a Streamlit interface, and the model will generate a relevant caption.


## Model Architecture

- **ResNet50**: A 50-layer deep convolutional neural network that serves as the **vision backbone**. It extracts visual features from the image.
- **BLIP**: A Transformer-based model that integrates image features and generates natural language descriptions. It leverages both visual and textual understanding.

---

##  Features

- 📷 Upload any image through the Streamlit interface.
- 🧠 Generate captions.
- ⚡ Powered by pretrained models.
- 🌐 Deployed as a live web app using Streamlit.
- 🔌 Lightweight and easy to run locally.

---

### Requirements
```bash

pip install -r requirements.txt

```

How to Run the APP
```bash
streamlit run app.py
```
 
## Project Demo 

![Screenshot 2025-01-02 213856](https://github.com/user-attachments/assets/96bd025d-62a4-449c-9162-20977325bea6)
![Screenshot 2024-12-21 220831](https://github.com/user-attachments/assets/6d66f615-7014-4618-b650-9af486bd0108) ![Screenshot 2024-12-21 221119](https://github.com/user-attachments/assets/e67d9d45-ae41-4c15-a8c5-2be6a7cee23e)
