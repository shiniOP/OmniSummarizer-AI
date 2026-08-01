import streamlit as st

from loaders.file_loader import extract_text
from loaders.url_loader import extract_url_text

from summarizer.chain import generate_ai_response

from utils.export import (
    create_txt,
    create_docx,
    create_pdf,
)

st.set_page_config(
    page_title="OmniSummarizer AI",
    page_icon="📝",
    layout="wide",
)

st.title("📝 OmniSummarizer AI")
st.write("Summarize text, documents, websites, and YouTube videos using LLM.")

# INPUT SOURCE
input_source = st.radio(
    "Choose Input Source",
    ["Paste Text", "Upload File", "URL"],
    horizontal=True,
)

# AI TASK
ai_task = st.selectbox(
    "AI Task",
    [
        "Summary",
        "Executive Summary",
        "Bullet Points",
        "Key Takeaways",
        "Explain Like I'm 5",
        "Keywords",
        "Question & Answer",
        "Mermaid Mind Map",
    ],
)

# Summary Options
col1, col2 = st.columns(2)

with col1:

    summary_length = st.selectbox(
        "Summary Length",
        [
            "Short",
            "Medium",
            "Detailed",
        ],
    )

with col2:

    summary_style = st.selectbox(
        "Summary Style",
        [
            "Paragraph",
            "Bullet Points",
            "Executive Summary",
        ],
    )


# Text Input
user_text = ""
uploaded_file = None
url = ""


# TEXT
if input_source == "Paste Text":

    user_text = st.text_area(
        "Paste your text here",
        height=300,
        placeholder="Paste your article, notes, research paper, or any text here...",
    )


# DOCUMENT
elif input_source == "Upload File":

    uploaded_file = st.file_uploader(
        "Upload a PDF, DOCX, or TXT file",
        type=["pdf", "docx", "txt"],
    )


# URL
elif input_source == "URL":

    url = st.text_input(
        "Enter Website or YouTube URL",
        placeholder="https://...",
    )


# Statistics
if input_source == "Paste Text":

    st.caption(
        f"Words: {len(user_text.split())} | Characters: {len(user_text)}"
    )


# GENERATE AI RESPONSE
if st.button("Generate"):

    try:

        # -------- TEXT --------

        if input_source == "Paste Text":

            if not user_text.strip():
                st.warning("Please enter some text.")
                st.stop()

        # -------- DOCUMENT --------

        elif input_source == "Upload File":

            if uploaded_file is None:
                st.warning("Please upload a document.")
                st.stop()

            user_text = extract_text(uploaded_file)

        # -------- URL --------

        elif input_source == "URL":

            if not url.strip():
                st.warning("Please enter a URL.")
                st.stop()

            user_text = extract_url_text(url)

        # -------- SHOW STATS --------

        st.caption(
            f"Words: {len(user_text.split())} | Characters: {len(user_text)}"
        )

        # -------- GENERATE --------

        with st.spinner("Generating AI response..."):

            response = generate_ai_response(
                text=user_text,
                task=ai_task,
                summary_length=summary_length,
                summary_style=summary_style,
            )

        st.subheader(ai_task)

        st.write(response)

        # -------- DOWNLOAD RESPONSE --------

        st.divider()

        st.subheader("📥 Download Response")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.download_button(
                label="📄 TXT",
                data=create_txt(response),
                file_name="response.txt",
                mime="text/plain",
            )

        with col2:

            st.download_button(
                label="📝 DOCX",
                data=create_docx(response),
                file_name="response.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        with col3:

            st.download_button(
                label="📕 PDF",
                data=create_pdf(response),
                file_name="response.pdf",
                mime="application/pdf",
            )

    except Exception as e:

        st.exception(e)


# ABOUT
with st.expander("ℹ️ About"):

    st.write(
        """
**OmniSummarizer AI** is an AI-powered content assistant built using:

- 🦜 LangChain (LCEL)
- 🤖 Gemini 2.5 Flash Lite
- 🎈 Streamlit

### Features

- ✅ Text Summarization
- ✅ PDF Summarization
- ✅ DOCX Summarization
- ✅ TXT Summarization
- ✅ Website Summarization
- ✅ YouTube Summarization

### AI Modes

- ✅ Summary
- ✅ Executive Summary
- ✅ Bullet Points
- ✅ Key Takeaways
- ✅ Explain Like I'm 5
- ✅ Keywords
- ✅ Question & Answer
- ✅ Mermaid Mind Map

### Export

- ✅ TXT
- ✅ DOCX
- ✅ PDF
"""
    )