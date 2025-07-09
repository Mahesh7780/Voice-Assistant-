from flask import Flask, request, render_template, jsonify
from agent.llm_setup import agent
import speech_recognition as sr
import pyttsx3
import os

app = Flask(__name__)

engine = pyttsx3.init()
engine.setProperty('rate', 180)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get("query")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        response = agent.run(user_input)
        speak(response)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/voice', methods=['POST'])
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        response = agent.run(text)
        speak(response)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
