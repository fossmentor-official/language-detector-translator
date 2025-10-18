# 🌍 Language Detector & Translator

A simple yet powerful **Natural Language Processing (NLP)** project built with **Streamlit** that can:

- 🔍 **Detect** the language of any input text using `langdetect`
- 🌐 **Translate** text into multiple languages using:
  - Google Translator (default)
  - LibreTranslate (open source)
  - Argos Translate (offline translation)
  - MyMemory Translator (backup option)

This app is fully containerized with a **Dev Container** setup, making it easy to run and extend in any environment.

---

## 🚀 Features

✅ Detect language instantly using AI-based language detection  
✅ Translate text into English, Arabic, French, Spanish, German, or Urdu  
✅ Automatically switch between multiple translation engines  
✅ Offline fallback using Argos Translate  
✅ Built with Streamlit for a clean, interactive UI  
✅ Fully Docker + Dev Container ready (VS Code compatible)

---

## 🧠 Tech Stack

| Category | Tool |
|-----------|------|
| Frontend UI | Streamlit |
| NLP Core | langdetect |
| Translators | Google Translator, LibreTranslate, Argos Translate, MyMemory |
| Containerization | Docker, VS Code Dev Container |

---

## 🏗️ Project Structure

language-detector-translator/
│
├── .devcontainer/
│ ├── devcontainer.json # VS Code Dev Container configuration
│ ├── Dockerfile # Docker image setup for the environment
│
├── app/
│ ├── main.py # Streamlit app (frontend logic)
│ ├── translator_utils.py # Translation logic and fallbacks
│ ├── requirements.txt # Python dependencies
│
├── README.md 


---

## ⚙️ Installation & Setup

### 🧩 Option 1: Run Locally (Without Docker)

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/language-detector-translator.git
   cd language-detector-translator

2. **Create a virtual environment**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Mac/Linux
  venv\Scripts\activate     # On Windows

3. **Install dependencies**
  ```bash
  pip install -r requirements.txt

4. **Run the Streamlit app**
  ```bash
  streamlit run app/main.py

### 🧩 Option 2: Run Inside Dev Container (Recommended)

This project comes with a .devcontainer setup for VS Code.

1. Open the project folder in VS Code
2. Make sure you have:
  * Docker Desktop running
  * VS Code extension: Dev Containers
3. Press Ctrl + Shift + P → “Dev Containers: Reopen in Container”
4. Once built, your app will run inside a fully isolated environment.
5. Start the app:
  ```bash
  streamlit run app/main.py

--------------------------------

<!-- Actual text -->
## Find me on
[![Facebook][1.2]][1] [![LinkedIn][2.2]][2] [![Instagram][3.2]][3]

<!-- Icons -->

[1.2]: https://i.imgur.com/dqSkGWu.png (Facebook)
[2.2]: https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/linkedin-3-16.png (LinkedIn)
[3.2]: https://i.imgur.com/TFy6wii.png (Instagram)

<!-- Links to my social media accounts -->
[1]: https://facebook.com/fossmentor
[2]: https://www.linkedin.com/in/fossmentor/
[3]: https://www.instagram.com/fossmentor.official/

## Having troubles implementing?
 > Reach out to me contact@fossmentor.com 
 I will be happy to assist 
# 
## want something improved or added?
  > Fork the repo @ [GitHub](https://github.com/fossmentor-official/ai-news-summarizer)
# 
## Regards,
 > [Fossmentor](https://fossmentor.com)


🪪 License
MIT License © 2025 Fossmentor Official
