
# 🎙️ AI Voice Assistant (Flask + LLM Agent + Voice Input/Output)

This is a voice-enabled AI assistant web application built using **Flask**, **SpeechRecognition**, **pyttsx3** (text-to-speech), and a custom **LLM agent** (from `agent.llm_setup`). It supports both text and voice interaction.

---

## 🚀 Features

- 🌐 Web-based UI (`index.html`)
- 📤 Send questions via text
- 🎤 Voice input support (speech-to-text using microphone)
- 🔊 Voice output response (text-to-speech using `pyttsx3`)
- 🤖 Integrated LLM agent for intelligent responses

---

## 🧱 Project Structure

```

your-project/
│
├── agent/
│   └── llm\_setup.py     # Your custom LLM agent setup
├── templates/
│   └── index.html       # Frontend UI
├── app.py               # Main Flask application
└── README.md            # This file

````

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
````

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, here are the main packages:

```bash
pip install flask SpeechRecognition pyttsx3 pyaudio
```

> ⚠️ **Note**: On Windows, `pyaudio` can be tricky. If you face installation issues, download the appropriate `.whl` from [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## 🧠 Configure the Agent

Ensure you have a working `agent/llm_setup.py` file that exports an `agent` object with a `.run(query)` method, such as:

```python
# agent/llm_setup.py
from some_llm_library import YourAgent

agent = YourAgent(api_key="your-api-key")
```

---

## ▶️ Running the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🗣️ Voice Usage

### 🎤 For Voice Input (POST to `/voice`)

Requires an active microphone.

Make sure your mic is connected and allowed. The `/voice` endpoint listens to your voice and responds via speech and text.

### 🔊 Text-to-Speech Output

Responses are read out using `pyttsx3`. Works offline and supports system TTS voices.

---

## ✅ Example Usage

```bash
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"query": "What is AI?"}'
```

---

## 📦 Optional: `requirements.txt`

```
Flask
SpeechRecognition
pyttsx3
pyaudio
```

---

## 🧑‍💻 Author

* 👤 **Mahesh G**
* 🔗 [GitHub](https://github.com/Mahesh7780)
