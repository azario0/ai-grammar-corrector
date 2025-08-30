import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- MODEL CONFIGURATION ---
try:
    # Configure the Gemini API with the key from the .env file
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)
    
    # Create the model
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("Gemini model loaded successfully.")
except Exception as e:
    print(f"Error initializing Gemini model: {e}")
    model = None

# --- LANGUAGE LIST ---
LANGUAGES = [
    "english", "french", "arabic", "spanish", "german", "italian", 
    "portuguese", "russian", "chinese (simplified)", "chinese (traditional)", 
    "japanese", "korean", "turkish", "hindi", "bengali", "urdu", "swahili", 
    "dutch", "greek", "polish"
]

def generate_correction(language, text):
    """
    Generates a grammatically corrected version of the text using the Gemini API.
    """
    if not model:
        return None, "The Gemini model could not be initialized. Please check your API key and configuration."

    prompt = f"""
    You are a professional grammar corrector.
    The following text is written in {language}.
    Your task: Correct any grammar, spelling, or punctuation mistakes, while keeping the original meaning and style.
    Return only the corrected text, without any explanations, introductions, or pleasantries.

    Original Text:
    "{text}"

    Corrected Text:
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip(), None
    except Exception as e:
        print(f"An error occurred during API call: {e}")
        return None, f"An error occurred while communicating with the Gemini API: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected_text = None
    original_text = ""
    selected_language = "english"
    error_message = None

    if request.method == 'POST':
        selected_language = request.form.get('language')
        original_text = request.form.get('user_text')
        
        if not original_text:
            error_message = "Please enter some text to correct."
        else:
            corrected_text, error_message = generate_correction(selected_language, original_text)

    return render_template(
        'index.html',
        languages=LANGUAGES,
        selected_language=selected_language,
        original_text=original_text,
        corrected_text=corrected_text,
        error=error_message
    )

if __name__ == '__main__':
    app.run(debug=True)