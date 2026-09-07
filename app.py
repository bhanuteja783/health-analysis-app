import streamlit as st
from PIL import Image, UnidentifiedImageError

from languages import LANGUAGES, translate_text
from logic import detect_diseases
from utils import extract_text_from_image


st.set_page_config(page_title="🩺 Health Report Analyzer")
st.title("🩻 Health Report Analyzer")
st.markdown(
    "Upload a medical report (JPG/PNG) and select a language to extract text and "
    "highlight supported health-related terms. This tool is not a medical diagnosis."
)

uploaded_file = st.file_uploader(
    "📎 Upload a health report image",
    type=["jpg", "jpeg", "png"],
)
selected_language = st.selectbox("🌐 Choose your language", LANGUAGES)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except (UnidentifiedImageError, OSError) as exc:
        st.error(f"Unable to read the uploaded image: {exc}")
    else:
        st.image(image, caption="Uploaded Report", use_container_width=True)

        with st.spinner("🔍 Analyzing report..."):
            extracted_text = extract_text_from_image(image)

        if extracted_text.startswith("Error extracting text:"):
            st.error(extracted_text)
        elif not extracted_text:
            st.warning("⚠ No readable text was found in the image.")
        else:
            st.subheader("📄 Extracted Report Text")
            st.code(extracted_text)

            diseases_found = detect_diseases(extracted_text)

            if not diseases_found:
                st.info("No supported health-related terms were detected.")
            else:
                st.subheader("🔎 Detected Health-Related Terms")
                for disease, advice in diseases_found.items():
                    st.markdown(f"🩺 **{disease.upper()}**")
                    translated = translate_text(advice, selected_language)
                    st.write(translated)

        st.caption(
            "Important: OCR and keyword matching can be inaccurate. Do not use this "
            "tool to diagnose, treat, or rule out a medical condition."
        )
