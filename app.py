from dotenv import load_dotenv
from PIL import Image
import os
import google.generativeai as genai
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Configure the generative AI model with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to prepare image data for processing
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        # Prepare image parts in the required format
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Function to get response from Gemini model
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Configure Streamlit page
st.set_page_config(page_title="Invoice Extractor", page_icon="📑", layout="centered")
st.header("📑 MultiLanguage Invoice Extractor")
st.markdown("""
   <div style='color: gray; font-size: 15px;'>
       Last updated on 04/07/2024.
   </div>
   """, unsafe_allow_html=True)
st.markdown("---")

# Input prompt for user
input_prompt = """You are an expert in understanding invoices. We will upload an image as invoice and you will have 
to answer any questions based on the uploaded invoice image"""

# User input for prompt
input = st.text_input("Input Prompt: ", key="input")

# File uploader for invoice image
uploaded_file = st.file_uploader("Choose an image of the invoice", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to trigger model response
submit = st.button("Tell me about the invoice")

# Process user request and display response
if submit:
    if uploaded_file is not None:
        try:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input)
            st.subheader("The Response is")
            st.write(response)
        except FileNotFoundError as e:
            st.error(str(e))
    else:
        st.warning("Please upload an invoice image.")