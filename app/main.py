# --------------------------------------------------------------
# 🌍 Language Detector & Translator App
# --------------------------------------------------------------
# This Streamlit app allows users to:
# 1️⃣ Detect the language of any input text using `langdetect`.
# 2️⃣ Translate the text into a selected target language using
#    multiple translation backends (Google, Libre, MyMemory, etc.).
# --------------------------------------------------------------

import streamlit as st
from langdetect import detect                # For language detection
from translator_utils import translate_text  # Custom helper for translation (multi-engine support)

# --------------------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------------------
st.set_page_config(page_title="🌍 Language Detector & Translator", layout="centered")

# --------------------------------------------------------------
# App Title and Description
# --------------------------------------------------------------
st.title("🌍 Language Detector & Translator")
st.write("Detect any language and translate text instantly using multiple translation engines.")

# --------------------------------------------------------------
# User Input Section
# --------------------------------------------------------------
# Text input area for user
text = st.text_area("✍️ Enter your text here:", height=150)

# Create a dictionary mapping full language names to their codes
languages = {
    "English (en)": "en",
    "Arabic (ar)": "ar",
    "French (fr)": "fr",
    "Spanish (es)": "es",
    "German (de)": "de",
    "Urdu (ur)": "ur"
}

# Streamlit dropdown to select full language name
selected_language = st.selectbox(
    "🌐 Select Target Language",
    list(languages.keys())
)

# Extract the corresponding language code
target_lang = languages[selected_language]

# --------------------------------------------------------------
# Action Buttons
# --------------------------------------------------------------
# Two-column layout for buttons
col1, col2 = st.columns(2)

with col1:
    detect_btn = st.button("🔍 Detect Language")  # Detect language button
with col2:
    translate_btn = st.button("🌐 Translate")      # Translate button

# --------------------------------------------------------------
# Language Detection Logic
# --------------------------------------------------------------
if detect_btn:
    if text.strip():  # Ensure text area isn't empty
        try:
            lang = detect(text)  # Perform language detection
            st.success(f"Detected language: **{lang.upper()}**")
        except Exception as e:
            st.error(f"Language detection failed: {e}")
    else:
        st.warning("Please enter some text first!")

# --------------------------------------------------------------
# Translation Logic
# --------------------------------------------------------------
if translate_btn:
    if text.strip():
        with st.spinner("Translating... please wait"):
            translated_text, info = translate_text(text, target_lang)

            if translated_text:
                # Display translation result and source engine
                if isinstance(info, list):
                    st.info(f"✅ Translated using: {info[0]}")
                st.success(translated_text)
            else:
                # Show fallback if all engines fail
                st.error("All translation engines failed 😞")
                with st.expander("Show Error Details"):
                    for err in info:
                        st.text(err)
    else:
        st.warning("Please enter some text first.")

# --------------------------------------------------------------
# Footer Section
# --------------------------------------------------------------
st.markdown("---")  # Horizontal line
st.markdown(
    """
    <div style="text-align:center; font-size:14px; color:#000;">
        🌟 Built with ❤️ using <b>Python</b> & <b>Streamlit</b> <br>
        ⚙️ Translation Engines: Google, LibreTranslate, MyMemory <br>
        👨‍💻 Developer: <a href="https://www.linkedin.com/in/fossmentor" target="_blank">FossMentor</a>
    </div>
    """,
    unsafe_allow_html=True
)
