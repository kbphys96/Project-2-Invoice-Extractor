from dotenv import load_dotenv

load_dotenv() #Load All the Environment Variable from .env File

import streamlit as st
import os 
import io
import base64
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemni Flash 
MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

# This function is no longer strictly needed if working directly with uploaded_file.read()
# However, if you need to perform additional image manipulations with Pillow, keep it.
# def pil_to_gemini_image(image):
#     buffered = io.BytesIO()
#     image.save(buffered, format="PNG")  # Save in memory
#     img_bytes = buffered.getvalue()
#     return {
#         "mime_type": "image/png",
#         "data": base64.b64encode(img_bytes).decode("utf-8")
#     }

def get_gemini_response(full_prompt_text, image_data): # Corrected function signature
    # The image_data is already in the correct format for the Gemini API
    # The prompt should include both the initial instruction and the user's specific question
    response = model.generate_content([full_prompt_text, image_data]) # Removed redundant `prompt` argument
    return response.text

##Initialize Stremalit App
st.set_page_config(page_title="Multi Language Invoice extractor")

st.header("Multi Language Invoice extractor")
input_prompt_text = st.text_input("Input Prompt",key="input_prompt_key") # Renamed to avoid clash with `input` variable later
uploaded_file=st.file_uploader("Choose an Image of Invoice...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_container_width=True) 

submit=st.button("Tell me about the invoice")

# The general instruction for the model
system_prompt='''You are an expert in understanding the Invoices. We will upload image as an invoice 
and you have to answer any question based on the uploaded Invoice'''

#If submit Button is clicked
if submit:
    if uploaded_file is not None:
        # Before reading the file for the API, ensure the pointer is at the beginning
        uploaded_file.seek(0) # IMPORTANT: Reset the file pointer

        # Convert the uploaded image into bytes for the API call
        image_data = {
            "mime_type": uploaded_file.type,
            "data": uploaded_file.read()
        }
        
        # Combine the system prompt and the user's input prompt
        full_prompt = f"{system_prompt}\n{input_prompt_text}"
        
        # Corrected call to get_gemini_response with only two arguments
        response = get_gemini_response(full_prompt, image_data) 

        st.subheader("The Response is..")
        st.write(response)
    else:
        st.warning("Please upload an invoice image first.")