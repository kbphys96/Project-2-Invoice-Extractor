Multi-Language Invoice Extractor 📄💬
This Streamlit app uses Google Gemini 1.5 Flash to extract and understand information from invoices in multiple languages. You can upload an invoice image, ask any question about it, and get AI-powered answers.

🚀 Features
Upload invoices in JPG, JPEG, or PNG format.

Works with multi-language invoices.

Uses Google Generative AI (Gemini) for accurate text extraction and interpretation.

Interactive Streamlit web interface.

🛠️ Tech Stack
Python

Streamlit – for the UI

Pillow (PIL) – for image handling

Google Generative AI SDK – to interact with Gemini API

dotenv – to manage environment variables

📂 Project Structure
bash
Copy
Edit
.
├── .gitignore
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── GST-Tax-Invoice-Format.jpg  # Sample invoice
├── Multi Language Invoice extractor.pdf  # Project reference doc
└── README.md               # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/kbphys96/multi-language-invoice-extractor.git
cd multi-language-invoice-extractor
2️⃣ Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set up environment variables
Create a .env file in the project root and add your Google API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
📸 Usage
Enter a prompt (e.g., "What is the total amount?").

Upload an invoice image.

Click Tell me about the invoice.

Get AI-generated responses instantly.

⚠️ Troubleshooting
InvalidArgument: empty inlineData – Ensure the image is properly read as bytes before sending to the API.

NameError: 'io' not defined – Add import io at the top of your script.

AttributeError: 'dict' object has no attribute 'save' – Ensure you are working with a PIL.Image object, not a dictionary.

📜 License
This project is licensed under the MIT License.

