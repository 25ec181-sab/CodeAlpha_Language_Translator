import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool")

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages using AI")

text = st.text_area("Enter text to translate")

source_lang = st.selectbox(
    "Select Source Language",
    ["auto", "en", "ta", "hi", "fr", "de", "es"]
)

target_lang = st.selectbox(
    "Select Target Language",
    ["en", "ta", "hi", "fr", "de", "es"]
)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text to translate")
    else:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)
        st.success("Translated Text:")
        st.write(translated)
