# MultiLanguage Invoice Extractor

[Explore Now](https://multi-language-invoice-extractor.streamlit.app/)

## Overview

The MultiLanguage Invoice Extractor is a web application built with Streamlit that leverages Google's Generative AI model to analyze and extract data from invoice images in multiple languages. Users can upload invoice images and receive insights based on the content.

## Features

- Upload invoice images (JPG, JPEG, PNG formats)
- Automatic content extraction and analysis
- User-friendly Streamlit interface
- Multi-language invoice processing support

## Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Required packages:
- streamlit
- google-generativeai
- python-dotenv

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Create a `.env` file in the root directory:

```
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

Replace `YOUR_GOOGLE_API_KEY` with your actual Google Generative AI API key.

## Usage

Run the application:

```bash
streamlit run app.py
```

Access the application at `http://localhost:8501` in your web browser.

## How It Works

1. Environment variables are loaded from the `.env` file
2. Google Generative AI model is configured with the API key
3. Users upload invoice images
4. The application processes the image to extract data
5. A response is generated based on the invoice content using the AI model

## File Structure

```
├── app.py             # Main application file
├── .env               # Environment variables file
└── requirements.txt   # Required Python packages
```

## Contributing
Contributions to enhance the analysis or extend the project are welcome. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For inquiries, suggestions, or feedback, please reach out to: [AryanShah30](https://github.com/AryanShah30)
