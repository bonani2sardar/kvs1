import streamlit as st
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def pdf_summarizer(text, num_sentences=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Filter out stop words
    word_freq = Counter([word for word in words if word.lower() not in stop_words])

    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    sentences = sent_tokenize(text)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split()) < 30:  # Prevent very long sentences from dominating the summary
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_freq[word]
                    else:
                        sentence_scores[sentence] += word_freq[word]

    # Get top 'num_sentences' sentences with highest scores
    summary_sentences = dict(sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences])
    summary = " ".join(summary_sentences.keys())
    return summary

def main():
    st.title("PDF Text Summarizer")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
        pdf_text = ""
        for page_num in range(pdf_reader.numPages):
            pdf_text += pdf_reader.getPage(page_num).extractText()

        st.header("Original PDF Text")
        st.write(pdf_text)

        num_sentences = st.slider("Number of Sentences in the Summary", min_value=1, max_value=10, value=3)

        if st.button("Summarize"):
            summary = pdf_summarizer(pdf_text, num_sentences)
            st.header("Summary")
            st.write(summary)

if __name__ == "__main__":
    main()
