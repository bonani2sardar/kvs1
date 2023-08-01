import streamlit as st
from transformers import pipeline

model_name = 'facebook/bart-large-cnn'
summarizer = pipeline('summarization',model=model_name,tokenizer=model_name)

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
            print(summary)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

    # Function to summarize the text
def summarize_text(text):
    '''
    text : string
    '''
    # Set the maximum length of the summary
    max_length = 130

    # Generate the summary
    # summarized_text = summarizer(text, max_length=max_length, min_length=0,clean_up_tokenization_spaces=True,no_repeat_ngram_size=4)
    # summarized_text = ' '.join([summ['summary_text'] for summ in summarized_text])
    summarized_text = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summarized_text

# Run the app
if __name__ == "__main__":
    main()
