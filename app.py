# Imports (same as before)
import streamlit as st
from PIL import Image
import google.generativeai as genai
from deep_translator.google import GoogleTranslator

# API (same as before)
API = "Put Your API Here"

genai.configure(api_key=API)
model = genai.GenerativeModel('gemini-pro-vision')

# Upload image section
uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])
pr = 'How can I improve the design of my room? And tell me what you see in the image'
button = st.button('Let\'s Go')

if uploaded_file and button:
    # Load the uploaded image
    img = Image.open(uploaded_file)

    # Generate content using the model
    response = model.generate_content([pr, img])

    # Display the original image
    st.image(img, caption="Original Image")

    # Display the generated text
    st.markdown(response.text)

    # Translate to Farsi (optional)
    translated = GoogleTranslator(source='auto', target='fa').translate(response.text)
    st.markdown(translated, unsafe_allow_html=True)  # Allow HTML for Farsi characters

# Info section (same as before)
st.info('Developed By : Ali Jahani satreyek@gmail.com')
