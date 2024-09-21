# SummaryForge

SummaryForge is an AI-powered PDF summarization tool built with Python and Streamlit. It allows users to upload any PDF document, specify their summarization needs, and get instant, customized summaries using OpenAI's GPT models. Perfect for researchers, students, and professionals looking to quickly extract key insights from lengthy documents.

## Features

- **PDF Upload**: Easy-to-use interface for uploading PDF files of any size.
- **Custom Summarization**: Users can specify how they want the document summarized, allowing for flexible and targeted summaries.
- **AI-Powered Analysis**: Utilizes OpenAI's GPT models (GPT-4 or GPT-3.5-Turbo) for high-quality, context-aware summarization.
- **Interactive Web Interface**: Built with Streamlit for a seamless, user-friendly experience.
- **Error Handling**: Robust error management to handle various PDF formats and potential API issues.
- **Environment Variable Support**: Secure API key management using environment variables.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/SummaryForge.git
   cd SummaryForge
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit app:
   ```
   streamlit run summarization_app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Upload a PDF file using the file uploader.

4. Enter your summarization request in the text area (e.g., "Summarize the key points in bullet points").

5. Click the "Summarize" button and wait for the AI-generated summary.

## How It Works

1. **PDF Processing**: The `extract_text_from_pdf` function in `summarization_lib.py` extracts text from the uploaded PDF using PyPDF2.

2. **OpenAI API Integration**: The `get_summary` function in `summarization_lib.py` sends the extracted text and user's summarization request to OpenAI's API.

3. **Streamlit Interface**: `summarization_app.py` creates an interactive web interface for file uploading and displaying results.

## Customization

- To change the OpenAI model, modify the `model` parameter in the `client.chat.completions.create` call in `summarization_lib.py`.
- Adjust the `max_tokens` and `temperature` parameters to control the length and creativity of the summaries.

## Contributing

Contributions to SummaryForge are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the GPT models
- Streamlit for the amazing web app framework
- PyPDF2 for PDF processing capabilities

## Disclaimer

This tool is for research and educational purposes only. Ensure you have the right to summarize any documents you upload, and be aware of potential confidentiality concerns when using external APIs for document processing.
