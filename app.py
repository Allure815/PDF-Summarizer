import streamlit as st
from pdf_utils import extract_text_from_pdf
from text_utils import clean_text, chunk_text
from summarizer import TextSummarizer

# ----------------------------
# App Config
# ----------------------------
st.set_page_config(page_title="PDF Summarizer", layout="centered")
st.title("📄 AI PDF Summarizer")
st.write("Upload a PDF file and get a clear, concise summary.")

# ----------------------------
# PDF Upload
# ----------------------------
uploaded_pdf = st.file_uploader("Upload your PDF", type=["pdf"])
summarize_clicked = st.button("🧠 Generate Summary")

# ----------------------------
# Load Summarizer (cached)
# ----------------------------
@st.cache_resource
def load_summarizer():
    return TextSummarizer()

summarizer = load_summarizer()

# ----------------------------
# Execution Control
# ----------------------------
if uploaded_pdf is None:
    st.info("Please upload a PDF file to continue.")
elif not summarize_clicked:
    st.info("Click **Generate Summary** to start summarization.")
else:
    try:
        with st.spinner("Reading PDF..."):
            raw_text = extract_text_from_pdf(uploaded_pdf)

        with st.spinner("Cleaning text..."):
            cleaned_text = clean_text(raw_text)

        with st.spinner("Splitting into chunks..."):
            chunks = chunk_text(cleaned_text)
        st.success(f"Text split into {len(chunks)} chunks.")

        summaries = []
        with st.spinner("Summarizing chunks..."):
            for i, chunk in enumerate(chunks, start=1):
                summary = summarizer.summarize_chunk(chunk)
                summaries.append(summary)

        final_summary = "\n\n".join(summaries)
        st.markdown("### 📝 Final Summary")
        st.write(final_summary)

    except Exception as e:
        st.error(str(e))
