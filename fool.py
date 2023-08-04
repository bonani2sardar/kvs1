import streamlit as st
import PyPDF2
from transformers import pipeline

# Load the summarization model
#summarizer = pipeline("summarization")
model_name = 'facebook/bart-large-cnn'
summarizer = pipeline('summarization',model=model_name,tokenizer=model_name)

def summarize_text(input_text):
    summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    st.title("Text and PDF Summarizer")

    # Sidebar
    st.sidebar.title("Options")
    file_type = st.sidebar.selectbox("Choose file type:", ["Text", "PDF"])

    # Text input
    if file_type == "Text":
        text_input = st.text_area("Enter your text here:")
        if st.button("Summarize Text"):
            if text_input.strip() != "":
                summary_text = summarize_text(text_input)
                st.subheader("Summary:")
                st.write(summary_text)
            else:
                st.warning("Please enter some text to summarize.")

    # PDF input
    else:
        pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if pdf_file is not None:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_text = ""
            for page_num in range(pdf_reader.getNumPages()):
                pdf_text += pdf_reader.getPage(page_num).extractText()

            if st.button("Summarize PDF"):
                if pdf_text.strip() != "":
                    summary_text = summarize_text(pdf_text)
                    st.subheader("Summary:")
                    st.write(summary_text)
                else:
                    st.warning("The PDF file does not contain any text.")

if __name__ == "__main__":
    main()


