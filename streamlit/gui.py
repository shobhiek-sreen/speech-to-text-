import streamlit as st

from speech2text import speech2text

st.title("🎙️➡📄 Speech to text convertor (using OpenAI API to access Whisper model)")

column_1, column_2, column_3, column_4 = st.columns([2, 4, 1, 1])

api_key = column_1.text_input(
    label="OpenAI API key", help="https://platform.openai.com/account/api-keys"
)
audio_file = column_2.file_uploader(
    label="Upload your audio file here",
    type=["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"],
    accept_multiple_files=False,
    help="Please upload only files smaller than 25 MB. Support for this will be added later.",
)

language = column_3.selectbox(label="Language (optional)", options=("cs", "en"))

if api_key != "" and audio_file is not None:
    convert = column_4.button("Convert")
else:
    convert = False

if convert:
    with st.spinner(text="Converting..."):
        text = speech2text(api_key=api_key, audio_file=audio_file, language=language)

    st.download_button("Download converted txt file", text, "converted.txt")
    st.write(text)
