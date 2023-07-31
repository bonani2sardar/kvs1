import streamlit as st
from transformers import pipeline

def main():
    st.title("Document Summarization App")
    st.subheader("Upload a Document")

    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.write("Original Document")
        st.write(file_contents)

        summary_button = st.button("Summarize")

        if summary_button:
            summarizer = pipeline("summarization")
            summary = summarizer(file_contents, max_length=100, min_length=30, do_sample=False)[0]['summary']
            st.subheader("Summary")
            st.write(summary)
if __name__ == '__main__':
    main()