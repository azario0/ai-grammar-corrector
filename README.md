# AI Grammar Corrector 🤖✨

A sleek, user-friendly web application built with Flask that leverages the power of Google's Gemini API to provide real-time grammar, spelling, and punctuation corrections for text in multiple languages.



## 📖 Table of Contents

- [About the Project](#about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [License](#-license)
- [Author](#-author)

## 🎯 About the Project

This application provides a simple and intuitive interface for users to improve their writing. Simply select a source language, paste your text, and let the Gemini AI model refine it. The project is designed to be lightweight, easy to set up, and a practical demonstration of integrating a powerful language model into a web service.

## ✨ Features

-   **Multi-Language Support**: Corrects grammar in over 20 languages, including English, Spanish, French, German, Chinese, and more.
-   **Real-Time Correction**: Get instant feedback powered by the cutting-edge Gemini 1.5 Flash model.
-   **Clean & Responsive UI**: A modern, single-page interface that looks great on both desktop and mobile devices.
-   **Secure API Key Handling**: Uses a `.env` file to keep your API key safe and out of the source code.
-   **Original Text Comparison**: Displays the corrected text alongside your original input for easy comparison.

## 🛠️ Tech Stack

-   **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
-   **AI Model**: [Google Gemini API](https://ai.google.dev/)
-   **Frontend**: HTML5, CSS3
-   **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+ and `pip` installed.
-   A Google Gemini API key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/azario0/ai-grammar-corrector.git
    cd ai-grammar-corrector
    ```

2.  **Create and activate a virtual environment:**
    -   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    -   Create a file named `.env` in the root of the project directory.
    -   Add your Gemini API key to this file:
        ```
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
    -   Replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual key.

## 🏃 Usage

1.  **Run the Flask application:**
    ```sh
    flask run
    ```
    Or alternatively:
    ```sh
    python app.py
    ```

2.  **Open your web browser** and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

3.  **Use the app:**
    -   Select your desired language from the dropdown menu.
    -   Enter or paste the text you want to correct into the text area.
    -   Click the "Correct Grammar" button.
    -   The corrected text will appear below the form.

## ⚙️ Configuration

The primary configuration is the `GEMINI_API_KEY` in the `.env` file. The application will not work without it.

-   **`GEMINI_API_KEY`**: Your secret API key for authenticating with the Google Gemini service.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 👤 Author

-   **azario0** - [GitHub Profile](https://github.com/azario0)