import streamlit as st
import pytesseract
from PIL import Image
import numpy as np
from utils import detect_diseases
from languages import translate_text, LANGUAGES

st.set_page_config(page_title="🩺 Health Report Analyzer")
st.title("🩻 Health Report Analyzer")
st.markdown("Upload a medical report (JPG/PNG) and select language to get health analysis and suggestions.")

uploaded_file = st.file_uploader("📎 Upload a health report image", type=["jpg", "jpeg", "png"])
selected_language = st.selectbox("🌐 Choose your language", LANGUAGES)

if uploaded_file is not None and selected_language:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(image, caption="Uploaded Report", use_column_width=True)

    with st.spinner("🔍 Analyzing report..."):
        extracted_text = pytesseract.image_to_string(img_array)

        st.subheader("📄 Extracted Report Text:")
        st.code(extracted_text)

        diseases_found = detect_diseases(extracted_text)

        if not diseases_found:
            st.warning("⚠️ No known health issues detected.")
        else:
            st.subheader("✅ Detected Health Issues:")
            for disease, advice in diseases_found.items():
                translated = translate_text(advice, selected_language)
                st.markdown(f"**🩺 {disease.upper()}**")
                st.write(translated)
