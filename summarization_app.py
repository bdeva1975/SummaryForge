import streamlit as st
import summarization_lib as glib

st.set_page_config(page_title="Document Summarization")
st.title("Document Summarization")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
input_text = st.text_area("How would you like the document summarized?")

summarize_button = st.button("Summarize", type="primary")

if summarize_button:
    if uploaded_file is not None:
        st.subheader("Summary")

        with st.spinner("Analyzing the document..."):
            try:
                response_content = glib.get_summary(input_text, uploaded_file)
                st.write(response_content)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please upload a PDF file before summarizing.")