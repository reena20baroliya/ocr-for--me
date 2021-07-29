import streamlit as st
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.title("OCR - Optical Character Recognition")
img = st.file_uploader("choose an file")
if img is not None:
  img_read = Image.open(img)
  st.image(img)
  op = pytesseract.image_to_string(img_read)
  st.write(op)
