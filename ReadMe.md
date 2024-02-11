# GODXR - Experience your kindgom
## AKA Speak2Create or GenDecor

## Introduction
Speak anything you want to make, and the application showcases a variety of products, with the functionality to download associated Vision Pro Object (USDZ) files directly. It includes a speech-to-text feature allowing users to name a product, which is then sent to a specified API to retrieve and display the corresponding Vision Pro file.

## Features
- Product Gallery: Display a list of product names with options to download their USDZ files.
- Speech-to-Text: Record the name of a product, transcribe it, and send the transcription to an external API.
- Dynamic USDZ File Retrieval: Use an API call to retrieve and display USDZ files based on the transcribed audio.

## Installation

### Prerequisites
- Python 3.7 or newer

### Setup
1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

`` pip install -r requirements.txt``

Running the Application
Launch the application by running:

bash
Copy code
streamlit run app.py
## Contributing

Contributions to the Streamlit USDZ Product Showcase are welcome. Please take a look at the contributing guidelines for more information.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Appendix 

Given the limitations of this environment for file generation and download, I'll guide you on how to create these files manually:

1. **Create `README.md`**: Copy the markdown content provided above into a new file named `README.md` in your project's root directory.
2. **Create `requirements.txt`**: Copy the list of packages from above into a new file named `requirements.txt` in your project's root directory.
3. **Create `packages.txt`** (if needed): Copy the detailed package list into a new file named `packages.txt` in your project's root directory. Adjust the versions as necessary for your project.

This setup will provide a solid foundation for your Streamlit app, ensuring that others can easily understand, install, and use your project.



## Explanation:
After transcribing the audio, send_to_api_and_display_usdz is called with the transcribed text.
This function makes a POST request to the specified API endpoint, sending the transcribed text as data.
Upon receiving a successful response, it extracts the USDZ file URL from the response and displays it as a downloadable link in the Streamlit app.
Error handling: It checks for a successful response status and informs the user if the retrieval fails.
## Important Notes:
Adjust the data payload according to the API's expected request format. The example assumes a simple structure where the transcribed text is sent directly, but your API might require a different format.
The API's response structure and how you extract the USDZ URL might vary. Modify the usdz_url = response.json().get('usdz_url') line based on the actual response structure from your API.
Ensure you handle API keys securely. Hardcoding them in your source code, as shown for simplicity, is not recommended for production applications. Consider using environment variables or other secure methods for storing and accessing sensitive keys.
