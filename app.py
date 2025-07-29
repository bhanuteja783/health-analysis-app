import streamlit as st
from PIL import Image
from utils import extract_text_from_image
from logic import analyze_health_data
from languages import translate_text, LANGUAGES

st.set_page_config(page_title="Health Analyzer", layout="centered")
st.title("🩺 Health Report Analyzer")

uploaded_image = st.file_uploader("Upload your medical report (image format only)", type=["jpg", "jpeg", "png"])
selected_lang = st.selectbox("Select Output Language", LANGUAGES.keys())

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Report", use_column_width=True)
    
    with st.spinner("Extracting and analyzing your report..."):
        raw_text = extract_text_from_image(image)
        results = analyze_health_data(raw_text)

        st.subheader("🧾 Report Summary:")
        for param, info in results.items():
            summary = f"\n📌 **{param}**: {info['value']} ({info['status']})\n\n💡 {info['suggestion']}\n"
            translated = translate_text(summary, LANGUAGES[selected_lang])
            st.markdown(translated)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit, Tesseract OCR, and ML")