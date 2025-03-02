import streamlit as st
import fitz  # PyMuPDF

# 🎨 Streamlit UI
st.write("""
         ### Welcome to the Streamlit Pdf to text converter App
         """)
st.title("📄 PDF Text Extractor")
st.write("Upload a PDF file to extract its text.")

# 📂 Upload PDF File
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    # 📖 Open PDF with PyMuPDF
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    extracted_text = ""  # Store extracted text

    for page_num in range(len(pdf_doc)):
        page = pdf_doc[page_num]
        extracted_text += f"\n\n--- Page {page_num+1} ---\n\n"
        extracted_text += page.get_text()

    # 📜 Display Extracted Text
    st.text_area("Extracted Text", extracted_text, height=400)

    # 💾 Download Extracted Text
    st.download_button(
        label="📥 Download Text File",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
