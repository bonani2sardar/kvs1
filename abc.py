import streamlit as st
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration

# Load the BART model and tokenizer
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# Streamlit app configuration
st.set_page_config(page_title="Document Summarizer", layout="wide")

# Define the Streamlit app
def main():
    st.title("Document Summarizer")
    st.write("Enter your text below:")

    # Text input box
    text = st.text_area("Text", height=300)

    if st.button("Summarize"):
        if text:
            # Perform summarization
            summary = summarize_text(text)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

# Function to summarize the text
def summarize_text(text):
    # Set the maximum length of the summary
    max_length = 150

    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

# Run the app
if __name__ == "__main__":
    main()
