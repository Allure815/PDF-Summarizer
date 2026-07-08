
**📄 AI PDF Summarizer**

An end-to-end PDF processing pipeline — upload a PDF, extract and clean its text, split it into model-ready chunks, and generate a summary — built with a modular architecture ready for a transformer-based summarization model.



**💡 Why This Matters**

Long PDFs — reports, research papers, study material — take real time to get through. This project automates the front half of that problem: reliably pulling clean, structured text out of any PDF and preparing it in chunks sized for downstream NLP, the same pipeline shape used in production document-intelligence and RAG systems.

Input: any PDF file → Output: cleaned text, chunked, and summarized section by section.
---


## Problem

Many PDFs such as reports, research papers, and study materials are long and time-consuming to read.
Manually going through these documents can take a lot of effort.

This project solves that problem by **automatically extracting and summarizing the most important information from a PDF file.**

---


**⚙️ Key Features**

📤 PDF upload via a simple Streamlit interface
📑 Robust text extraction across all pages using pypdf, with graceful handling of unreadable pages
🧹 Text cleaning (whitespace/newline normalization) to prepare raw extracted text for NLP
✂️ Smart chunking with LangChain's RecursiveCharacterTextSplitter (800-char chunks, 100-char overlap) so long documents are split without breaking sentences mid-thought
🧠 Per-chunk summarization, merged into one final summary
⚡ Cached model loading (@st.cache_resource) so the app stays responsive across repeated runs

----


## What This Project Does

* Upload a PDF document
* Extract text from the file
* Clean and preprocess the extracted content
* Split long text into manageable chunks
* Generate summaries for each chunk using an AI model
* Combine all summaries into a final readable summary

---


**🧠 How It Works**


-User uploads a PDF through the Streamlit UI

-Text is extracted page-by-page with pypdf

-Extracted text is cleaned (normalized whitespace, stripped formatting noise)

-Cleaned text is split into overlapping chunks sized for model input limits

-Each chunk is summarized and all chunk summaries are combined into one final output


Current state: the summarization step uses a lightweight extractive placeholder (first-sentences heuristic) so the full pipeline runs end-to-end without a model download. The architecture is already wired for a transformer-based summarizer — transformers/torch are in the dependency stack — swapping in a model like facebook/bart-large-cnn or distilbart-cnn is the immediate next step (see below).

----



## Tech Stack

-PDF Extraction: pypdf
-Chunking: LangChain (RecursiveCharacterTextSplitter)
-Interface: Streamlit
-Language: Python
-Planned: HuggingFace Transformers, PyTorch (abstractive summarization model)

---

### Demo Video

Demo Video Link
https://github.com/Allure815/PDF-Summarizer/blob/main/Demo-Pdf.mp4
---

### Project Screenshot
https://github.com/Allure815/PDF-Summarizer/blob/main/PDF-ss.png
---



## Use Cases

* Quickly reviewing long documents
* Summarizing reports or research papers
* Extracting key insights from PDFs
* Learning project for AI-powered document processing

---



**▶️ Run It Locally**

bash# Clone
git clone https://github.com/Allure815/PDF-Summarizer.git
cd PDF-Summarizer

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py

Upload a PDF and click Generate Summary to run the full pipeline.

----



**🔭 What's Next**


Swap the placeholder summarizer for a real HuggingFace abstractive summarization model (facebook/bart-large-cnn or a lighter distilbart variant) — top priority, dependencies are already in place
Add downloadable summary output (PDF/TXT export)
Support multi-document summarization in a single session
Add chunk-level source tracking so each summary line can be traced back to its page

---



**👤 Author**

Heeral — https://github.com/Allure815

---
