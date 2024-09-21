import os
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2
from io import BytesIO

# Load environment variables from .env file
load_dotenv()

def get_summary(input_text, pdf_file):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Extract text from the uploaded PDF file
    pdf_text = extract_text_from_pdf(pdf_file)

    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant tasked with analyzing documents and answering questions about them."
        },
        {
            "role": "user",
            "content": f"Here's the content of the uploaded document:\n\n{pdf_text}\n\nBased on this document, please {input_text}"
        }
    ]

    chat_completion = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you prefer
        messages=messages,
        max_tokens=2000,
        temperature=0
    )

    return chat_completion.choices[0].message.content

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Example usage
if __name__ == "__main__":
    # This part won't be used in the Streamlit app, but kept for testing purposes
    with open("sample.pdf", "rb") as file:
        summary = get_summary("summarize the key points of this document.", file)
    print(summary)